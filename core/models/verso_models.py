"""
Stable import path for VERSO tables (``sites.verso`` app). Definitions remain in
``sites/verso/models.py``; this module re-exports them as an extension of core.
"""

from sites.verso.models import VersoArticle, VersoCategory

__all__ = ["VersoArticle", "VersoCategory"]
