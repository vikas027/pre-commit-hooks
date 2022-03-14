''' Check if commits are compliant with conventional commits '''

from __future__ import annotations

import argparse
from hooks.check_tool import is_tool
from hooks.run_cmd import main as cmd


def main(argv: Sequence[str] | None = None) -> int:
    ''' Main function called by the hook and
        return the exit code depending on success or failure
    '''
    parser = argparse.ArgumentParser(
        description='Checks compliance of conventional commits')
    parser.add_argument('--dry-run', dest='dry_run',
                        action='store_true',
                        help='Dry run of conventional commit check.')
    parser.add_argument('-t', '--ticket-prefix', dest='ticket_prefix',
                        default=None,
                        help="Ticket Number Prefix E.g. 'JIRA-'")
    args = parser.parse_args(argv)

    # Default Return Value
    ret_val = 1

    # Check if tool is present
    tool_name = 'commitsar'
    if not is_tool(tool_name):
        print(f'Executable not found : {tool_name}')
        return ret_val

    # Do not error out if dry run is enabled
    if args.dry_run:
        print('Dry Run is enabled')
        ret_val = 0

    # Check Commitsar output
    cmd_res = cmd('commitsar')
    print(cmd_res.stderr.decode('utf-8'))
    print(cmd_res.stdout.decode('utf-8'))
    if cmd_res.returncode == 1:
        return ret_val
    if 'commits are conventional commit compliant' not in cmd_res.stderr.decode("utf-8"):
        return ret_val

    # Check if Ticket Tool Prefix is present
    if args.ticket_prefix:
        print(f'Checking for Prefix in commit msg head: {args.ticket_prefix}')
        cmd_res = cmd('git show-branch --no-name HEAD')
        if cmd_res.returncode == 1:
            return ret_val
        if args.ticket_prefix not in cmd_res.stdout.decode('utf-8'):
            print(f'Ticket Prefix not found: {args.ticket_prefix}')
            return ret_val

    ret_val = 0
    return ret_val


if __name__ == '__main__':
    raise SystemExit(main())
