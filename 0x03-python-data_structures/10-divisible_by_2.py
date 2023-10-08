#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    times = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            times.append(True)
        else:
            times.append(False)
    return (times)
