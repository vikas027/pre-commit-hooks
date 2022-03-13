from __future__ import annotations

def is_tool(name):
    '''Check whether a tool is in $PATH and marked as executable'''
    from shutil import which
    return which(name) is not None
