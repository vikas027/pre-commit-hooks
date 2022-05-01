''' Make the folder a package '''

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("hooks")
except PackageNotFoundError:
    __version__ = "0.0.0"
