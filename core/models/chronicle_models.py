"""Re-export Chronicle models from ``sites.chronicle`` for a stable ``core`` namespace."""

from sites.chronicle.models import ChronicleEntry, ChronicleTag

__all__ = ["ChronicleEntry", "ChronicleTag"]
