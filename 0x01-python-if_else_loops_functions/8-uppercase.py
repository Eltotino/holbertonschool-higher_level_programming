#!/usr/bin/python3
def uppercase(str):
    for i in str:
        tmp = ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            tmp = ord(i) - 32

        print("{:c}".format(tmp), end="")
    print()
