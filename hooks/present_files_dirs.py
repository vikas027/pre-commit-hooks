''' Check if files and directories exists '''

from __future__ import annotations

import argparse
import os


def main(argv: Sequence[str] | None = None) -> int:
    ''' Main function called by the hook and
        return the exit code depending on success or failure
    '''
    parser = argparse.ArgumentParser(
        description='Checks existence of files and directories')
    parser.add_argument('--dry-run', dest='dry_run',
                        action='store_true',
                        help='Dry run of conventional commit check.')
    parser.add_argument('-l', '--list', dest='files_dirs_list',
                        default=None,
                        help="List of Files and Directories (must end with '/')")
    args = parser.parse_args(argv)

    # Default Return Value
    ret_val = 0

    if not args.files_dirs_list:
        print('List cannot be empty')
        return 1

    print('Checking if specified files and directories are present')
    for f_name in args.files_dirs_list.split(','):
        found = 0
        if f_name[-1] == '/' and os.path.isdir(f_name) is False:
            found = 1
        if f_name[-1] != '/' and os.path.isfile(f_name) is False:
            found = 1
        if found == 1:
            ret_val = 1
            print(f'File or directory not found: {f_name}')
            break

    # Do not error out if dry run is enabled
    if args.dry_run:
        print('Dry Run is enabled')
        ret_val = 0

    return ret_val


if __name__ == '__main__':
    raise SystemExit(main())
