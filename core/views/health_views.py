from django.http import HttpResponse


def health(request):
    """Liveness probe for load balancers (no database access)."""
    return HttpResponse("ok\n", content_type="text/plain; charset=utf-8")
