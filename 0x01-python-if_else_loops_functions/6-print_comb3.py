#!/usr/bin/python3
for digit_a in range(0, 10):
    for digit_b in range(digit_a + 1, 10):
        if digit_a == 8 and digit_b == 9:
            print("{}{}".format(digit_a, digit_b))
        else:
            print("{}{}".format(digit_a, digit_b), end=", ")
