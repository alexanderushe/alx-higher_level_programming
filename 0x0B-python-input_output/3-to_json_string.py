#!/usr/bin/python3

"""defines a string to json  function"""

import json

def to_json_string(my_obj):
    """returns json string containing objects' representation
    -> handles no exceptions in serialization process"""

    return json.dumps(my_obj)
