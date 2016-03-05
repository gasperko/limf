#!/bin/env python
"""Parses given arguments"""
import random
from .decrypter import decrypt_files
from .encrypter import encrypt_files
from .uploader import upload_files
from .hostlist import generate_host_string

def parse_arguments(args, clone_list):
    """
    Makes parsing arguments a function.
    """
    host_number = args.host

    if args.show_list:
        print(generate_host_string(clone_list, "Available hosts: "))
        exit()

    if args.decrypt:
        for i in args.files:
            print(decrypt_files(i))
            exit()
    if args.files:
        for i in args.files:
            if host_number is None or args.host != host_number:
                host_number = random.randrange(0, len(clone_list))
            while True:
                try:
                    if args.encrypt:
                        print(encrypt_files(clone_list[host_number], args.only_link, i))
                    else:
                        print(upload_files(open(i, 'rb'), \
                              clone_list[host_number], args.only_link, i))
                except IndexError:
                    #print('Selected server (' + clone_list[host_number][0] + ') is offline.')
                    #print('Trying other host.')
                    host_number = random.randrange(0, len(clone_list))
                    continue
                except IsADirectoryError:
                    print('limf does not support directory upload, if you want to upload ' \
                          'every file in directory use limf {}/*.'.format(i.replace('/', '')))
                break
    else:
        print("limf: try 'limf -h' for more information")
