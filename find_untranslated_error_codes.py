#!/usr/bin/env python

import argparse

def read_fields_into_list(path_fields_file):
    with open(path_fields_file) as fields_file:
        fields = fields_file.readlines()
    fields = [field.strip() for field in fields]
    return fields

def find_untranslated_fields(path_file_all_fields, path_file_translated_fields):
    """Returns the list of untranslated fields
    """
    all_fields = read_fields_into_list(path_file_all_fields)
    translated_fields = read_fields_into_list(path_file_translated_fields)
    
    return list(set(all_fields).difference(set(translated_fields)))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find the untranslated fields, given a file FILE_ALL_FIELDS with all the fields, and a file FILE_TRANSLATED_FIELDS with the fields that have already been translated')
    parser.add_argument('file_all_fields', metavar='FILE_ALL_FIELDS', type=str,
                        help='the FILE_ALL_FIELDS that contains all the fields, both translated and untranslated')
    parser.add_argument('file_translated_fields', metavar='FILE_TRANSLATED_FIELDS', type=str,
                        help='the FILE_TRANSLATED_FIELDS that contains only the fields that have been translated')
    args = parser.parse_args()

    untranslated_fields = find_untranslated_fields(args.file_all_fields, args.file_translated_fields)
    for field in untranslated_fields:
        print field
