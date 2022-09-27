#!/usr/bin/python3
"""Defines a json to object function"""
import json


def from_json_string(my_str):
    """Returns the python object represention of a JSON string"""
    return json.loads(my_str)
