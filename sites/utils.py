from importlib import import_module


def import_callable(dotted_path: str):
    """Import a view or other callable from 'package.module.viewname'."""
    module_path, name = dotted_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, name)
