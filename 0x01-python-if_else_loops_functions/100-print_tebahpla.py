#!/usr/bin/python3
for i in range(ord('z'), ord('a') -1):
    print("{:c}".format((i - 32) if c % 2 else c, end=""))