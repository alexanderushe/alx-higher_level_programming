#!/usr/bin/python3

import json

def to_json_string(my_obj):
    """returns json string containing objects' representation
    -> handles no exceptions in serialization process"""

    return json.dumps(my_obj)
