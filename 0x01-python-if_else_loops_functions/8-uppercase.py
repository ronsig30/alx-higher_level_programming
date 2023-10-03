#!/usr/bin/python3
def uppercase(str):
    for h in str:
        if ord(h) >= 97 and ord(h) <= 122:
            h = chr(ord(h) - 32)
        print("{}".format(h), end="")
    print("")
