import pkg_resources

__version__ = pkg_resources.get_distribution("netinv").version

__all__ = ("__version__",)
