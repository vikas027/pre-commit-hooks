from __future__ import annotations

import argparse
from hooks.check_tool import is_tool




def main(argv: Sequence[str] | None = None) -> int:
    ''' Main function called by the hook and
        return the exit code depending on success or failure
    '''
    parser = argparse.ArgumentParser(
        description='Checks compliance of conventional commits')
    parser.add_argument(
        'files', nargs='+', help='Not sure why the hook fails without this')  # To Fix Later
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

    if args.dry_run:
        print('Dry Run is enabled')
    if not args.dry_run:
        print('Dry Run is disabled')

    print(f"Ticket Prefix {args.ticket_prefix}")
    ret_val = 0
    # if args.ticket_prefix:
    #     print(f"Ticket Prefix {args.ticket_prefix}")
    # if not args.ticket_prefix:
    #     print(f"Ticket Prefix {args.ticket_prefix}")

    return ret_val


if __name__ == '__main__':
    raise SystemExit(main())
