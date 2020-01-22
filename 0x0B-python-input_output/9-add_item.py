#!/usr/bin/python3
"""This module contains a script which saves all arguments to a JSON object in
a file"""
import sys
save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file


def main():
    """Gets all arguments and appends them to the given list"""
    try:
        l = load_from_json_file("add_item.json")
    except:
        l = []
    l.extend(sys.argv[1:])
    save_to_json_file(l, "add_item.json")

if __name__ == "__main__":
    main()
