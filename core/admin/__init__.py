from django.contrib import admin

import core.admin.user_admin  # noqa: F401

from core.admin.content_admin import WebsiteContentAdmin
from core.admin.search_admin import SearchIndexAdmin
from core.models.content_models import WebsiteContent
from core.models.search_models import SearchIndex

admin.site.register(SearchIndex, SearchIndexAdmin)
admin.site.register(WebsiteContent, WebsiteContentAdmin)
