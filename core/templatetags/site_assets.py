from django import template
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def site_logo_url(slug: str) -> str:
    """Static URL for a subsite mark: sites/<slug>/static/<slug>/logo.svg."""
    return static(f"{slug}/logo.svg")
