''' Check if a tools exists or not '''

import subprocess


def main(cmd):
    '''Check whether a tool is in $PATH and marked as executable'''
    cmd_res = subprocess.run(cmd, shell=True, capture_output=True)
    return cmd_res
