''' Check if a tools exists or not '''

from __future__ import annotations

from shutil import which


def is_tool(name):
    '''Check whether a tool is in $PATH and marked as executable'''
    return which(name) is not None
