#!/bin/env python
"""A command line tool for uploding stuff to pomf.se clones"""
import argparse
from .parse_arguments import parse_arguments
from .hostlist import retrieve_online_host_list
from .hostlist import generate_host_string
from .hostlist import retrieve_local_host_list

def main():
    """Creates arguments and parses user input"""
    clone_list = retrieve_local_host_list('host_list.json')  # retrieve_online_host_list()
    host_string = generate_host_string(clone_list)

    parser = argparse.ArgumentParser(
        description='Uploads selected file to working pomf.se clone')
    parser.add_argument('files', metavar='file', nargs='+', type=str,
                        help='Files to upload')
    parser.add_argument('-c', metavar='host number', type=int,
                        dest='host', default=None,
                        help=host_string)
    parser.add_argument('-l', dest='only_link', action='store_const',
                        const=True, default=False,
                        help='Changes output to just link to the file')
    parser.add_argument('-e', dest='encrypt', action='store_const',
                        const=True, default=False,
                        help='Encrypts then uploads the files.')
    parser.add_argument('-d', dest='decrypt', action='store_const',
                        const=True, default=False,
                        help='Decrypts files from links with encrypted files')
    parser.add_argument('-j', dest="use_local_list",
                        default=False,
                        help='choose to use a local list')

    args = parser.parse_args()
    if args.host and args.host not in range(0, len(clone_list)):
        print('Please input valid host number')
        exit()
    try:
        if args.use_local_list:
            print("using local list @ {0}".format(args.use_local_list))
            clone_list = retrieve_local_host_list(args.use_local_list)
        else:
            clone_list = retrieve_online_host_list()
        parse_arguments(args, clone_list)
    except FileNotFoundError:
        print('Plese enter valid file.')

if __name__ == '__main__':
    main()
