#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        variale = fct(*args)
        return (variable)
    except Exception as e:
        sys.stderr.write(f"Exception: {e}\n")
        return (None)
