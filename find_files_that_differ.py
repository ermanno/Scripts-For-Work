#!/usr/bin/env python

import fnmatch
import os
import argparse
import pprint
import hashlib
from collections import defaultdict

def find_files_to_diff(directory, pattern):
    """
    Find all files in `directory' matching a given `pattern', searching recursively.
    """
    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

def hash(file_path):
    """
    Produce a md5 hash of the file contents.
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file_to_hash:
        buf = file_to_hash.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_different_files(files):
    """
    Return a map of files, that groups together equal files.
    """
    groups = defaultdict(list)
    for file_path in files:
        groups[hash(file_path)].append(os.path.abspath(file_path))
    return groups

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find the files named PATTERN that differ, starting the search from a given DIRECTORY and proceding recursively.')
    parser.add_argument('directory', metavar='DIRECTORY', type=str,
                        help='the root DIRECTORY from where to start the recursive search')
    parser.add_argument('pattern', metavar='PATTERN', type=str,
                        help='the PATTERN to search for')
    args = parser.parse_args()

    matches = find_files_to_diff(args.directory, args.pattern)
    groups = find_different_files(matches)

    pp = pprint.PrettyPrinter()
    pp.pprint(dict(groups))

    
