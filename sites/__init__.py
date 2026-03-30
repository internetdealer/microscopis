"""
Site packages live under this folder (views, templates, static, optional urls).

``verso`` and ``chronicle`` are Django apps under ``sites`` (``sites.verso``,
``sites.chronicle``) with their own models and migrations. Other site folders may
remain non-app packages routed via ``sites/registry.py`` and ``site_router``.
"""
