#!/bin/sh
set -e
cd /app
export DJANGO_SETTINGS_MODULE="${DJANGO_SETTINGS_MODULE:-microscopis.settings.production}"
MR="${MEDIA_ROOT:-/app/media}"
mkdir -p "$MR"

# Wait for PostgreSQL to accept connections (see docker-compose healthcheck)
i=0
while [ "$i" -lt 60 ]; do
  if python -c "
import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE', 'microscopis.settings.production'))
import django
django.setup()
from django.db import connection
try:
  connection.ensure_connection()
except Exception as e:
  sys.exit(1)
sys.exit(0)
" 2>/dev/null; then
    break
  fi
  i=$((i + 1))
  sleep 1
done
if [ "$i" -eq 60 ]; then
  echo "database did not become available in time" >&2
  exit 1
fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# First boot on an empty database: load SearchIndex and all site seeds (set SKIP_AUTO_SEED=1 to opt out).
# Do not re-run on every start; seed_microscopis deletes WebsiteContent, so we only run when the index is empty.
if [ "${SKIP_AUTO_SEED:-0}" != "1" ]; then
  if python -c "
import os, sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.environ.get('DJANGO_SETTINGS_MODULE', 'microscopis.settings.production'))
import django
django.setup()
from core.models.search_models import SearchIndex
sys.exit(0 if SearchIndex.objects.exists() else 1)
" 2>/dev/null; then
    : # already seeded
  else
    echo "docker-web-entrypoint: empty SearchIndex; running seed_microscopis (first start)..." >&2
    python manage.py seed_microscopis
  fi
fi

# Gunicorn default timeout is 30s; idle or half-open TCP (common with desktop browsers
# / Docker networking) can hit that and log WORKER TIMEOUT. Override via GUNICORN_TIMEOUT.
# Single any-address bind. Do not add --bind [::]:8000 as well: on Linux that often conflicts
# with 0.0.0.0 (Address already in use). Use http://127.0.0.1:8000 if localhost misbehaves.
#
# GUNICORN_WORKER_CLASS: default `sync`. Set `gthread` for I/O-bound apps under slow Docker
# I/O (e.g. macOS): uses --threads; default 1 process + 6 threads for gthread, 3 sync workers.
GWC="${GUNICORN_WORKER_CLASS:-sync}"
if [ "$GWC" = "gthread" ]; then
  GWRK="${GUNICORN_WORKERS:-1}"
  GTHR="--threads ${GUNICORN_THREADS:-6}"
else
  GWRK="${GUNICORN_WORKERS:-3}"
  GTHR=
fi
exec gunicorn microscopis.wsgi:application \
  --bind 0.0.0.0:8000 \
  -k "$GWC" $GTHR \
  --workers "$GWRK" \
  --timeout "${GUNICORN_TIMEOUT:-120}" \
  --access-logfile - \
  --error-logfile -

