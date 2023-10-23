#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        variale = fct(*args)
        return (variable)
    except Exception as f:
        print("Exception: {}".format(f), file=sys.stderr)
        return (None)
