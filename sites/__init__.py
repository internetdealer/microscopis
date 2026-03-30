"""
Site packages live under this folder (views, templates, static, optional urls).

``verso`` is registered as a Django app (``sites.verso``) so editorial content
uses database models in ``sites/verso/models.py``. Other site folders may
remain non-app packages routed via ``sites/registry.py`` and ``site_router``.
"""
