"""
Map URL slug (hyphenated, as in SearchIndex.website_slug) to a view callable.

Format: "slug": "dotted.path.to.module.view_function"

Add a line here when you drop a new folder under sites/ and want a custom view
instead of the DB-backed fallback.
"""

SITE_VIEWS: dict[str, str] = {}
