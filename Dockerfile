# App image: Gunicorn, Celery worker/beat, and management commands
FROM python:3.12-slim-bookworm

ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq5 \
        curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# collectstatic for WhiteNoise (dummy secrets; real env at runtime)
ENV DJANGO_SETTINGS_MODULE=microscopis.settings.production \
    DJANGO_SECRET_KEY=build-time-only \
    ALLOWED_HOSTS=localhost,127.0.0.1
RUN python manage.py collectstatic --noinput

RUN useradd --create-home --uid 1000 appuser \
    && chown -R appuser:appuser /app \
    && chmod +x /app/scripts/docker-web-entrypoint.sh
USER appuser

# Web-only: override CMD for celery/beat/flower. Healthcheck is on the `web` service in docker-compose.
EXPOSE 8000 5555
CMD ["/app/scripts/docker-web-entrypoint.sh"]
