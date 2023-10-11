#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_integers = set()
    results = 0

    for num in my_list:
        if num not in uniq_integers:
            result += num
            uniq_integers.add(num)

    return (result)
