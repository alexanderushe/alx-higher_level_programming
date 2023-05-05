#!/usr/bin/python3

"""Defines a json-to-object function"""
import json

def from_json_string(my_str):
    """return the python object representation of a json string"""
    return json.loads(my_str)
