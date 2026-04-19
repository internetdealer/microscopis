"""Set short public Cache-Control for anonymous HTML GETs (production only)."""

from __future__ import annotations

from django.conf import settings
from django.utils.cache import patch_cache_control


class PublicCacheControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.max_age = int(getattr(settings, "PUBLIC_CACHE_MAX_AGE", 0))

    def __call__(self, request):
        response = self.get_response(request)
        if self.max_age <= 0:
            return response
        if request.method != "GET" or response.status_code != 200:
            return response
        path = request.path
        if path.startswith("/static/"):
            return response
        admin_prefix = f"/{getattr(settings, 'ADMIN_URL', 'admin')}/"
        if path.startswith(admin_prefix):
            return response
        if path in ("/health", "/health/"):
            patch_cache_control(response, no_cache=True, must_revalidate=True, private=True)
            return response
        if getattr(request, "user", None) and request.user.is_authenticated:
            patch_cache_control(response, private=True, must_revalidate=True)
            return response
        content_type = (response.get("Content-Type") or "").split(";")[0].strip().lower()
        if content_type and content_type != "text/html":
            return response
        patch_cache_control(response, public=True, max_age=self.max_age)
        return response
