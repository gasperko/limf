#!/bin/env python
"""A command line tool for uploding stuff to pomf.se clones"""
import argparse
from .parse_arguments import parse_arguments
from .hostlist import retrieve_online_host_list
from .hostlist import generate_host_string
from .hostlist import retrieve_local_host_list

def main():
    """Creates arguments and parses user input"""
    parser = argparse.ArgumentParser(
        description='Uploads selected file to working pomf.se clone')
    parser.add_argument('files', metavar='file', nargs='*', type=str,
                        help='Files to upload')
    parser.add_argument('-c', metavar='host_number', type=int,
                        dest='host', default=None,
                        help='The number (0-n) of the selected host (default is random)')
    parser.add_argument('-l', dest='only_link', action='store_const',
                        const=True, default=False,
                        help='Changes output to just link to the file')
    parser.add_argument('-e', dest='encrypt', action='store_const',
                        const=True, default=False,
                        help='Encrypts then uploads the files.')
    parser.add_argument('-d', dest='decrypt', action='store_const',
                        const=True, default=False,
                        help='Decrypts files from links with encrypted files')
    parser.add_argument('-j', dest="local_list",
                        default=False, help='Path to a local list file')
    parser.add_argument('-s', dest="show_list", action='store_const',
                        const=True, default=False,
                        help='Show the host list (will not upload your files when called)')

    args = parser.parse_args()
    try:
        if args.local_list:
            clone_list = retrieve_local_host_list(args.local_list)
        else:
            clone_list = retrieve_online_host_list()

        if args.host and not(0 <= args.host < len(clone_list)):
            print(generate_host_string(clone_list))
            exit()

        parse_arguments(args, clone_list)
    except FileNotFoundError:
        print('Plese enter valid file.')

if __name__ == '__main__':
    main()
