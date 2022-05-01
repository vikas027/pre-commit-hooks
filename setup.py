''' Setup hooks module '''

from __future__ import annotations
from setuptools import setup
from hooks import __version__

NAME = "hooks"

if not __version__:
    raise ValueError("Can't find the version in {NAME}/__init__.py")


def myversion():
    ''' Return the clean version based on the branch '''
    from setuptools_scm.version import SEMVER_MINOR, guess_next_simple_semver, release_branch_semver_version

    def my_release_branch_semver_version(version):
        ver = release_branch_semver_version(version)
        if ver == version.format_next_version(guess_next_simple_semver, retain=SEMVER_MINOR):
            return version.format_next_version(guess_next_simple_semver, fmt="{guessed}", retain=SEMVER_MINOR)
        return ver

    return {
        'version_scheme': my_release_branch_semver_version,
        'local_scheme': 'no-local-version',
    }


setup(
    name=NAME,
    use_scm_version=myversion,
    # use_scm_version={
    #     'version_scheme': 'release-branch-semver',
    #     # 'write_to': '_version.py',
    #     # 'write_to_template': '__version__ = "{version}"',
    #     # 'tag_regex': r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$',
    # },
    setup_requires=['setuptools_scm'],
)
