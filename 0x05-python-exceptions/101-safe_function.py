#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        variale = fct(*args)
        return (variable)
    except Exception as f:
        print("Exception: {}".format(f), file=sys.stderr)
        return (None)
