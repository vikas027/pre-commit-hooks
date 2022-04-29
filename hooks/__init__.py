from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution("hooks").version
except DistributionNotFound:
    __version__ = None

del get_distribution, DistributionNotFound
