#!/usr/bin/pyton3

"""Defines a json file writing function"""
import json

def save_to_json_file(my_obj, filename):
    """write an object to a text file using JSON representation"""
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(json.dumps(my_obj))
