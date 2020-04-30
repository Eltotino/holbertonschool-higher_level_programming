#!/usr/bin/python3
if __name__ == "__main__":
    import sys
arglist = sys.argv
num = len(arglist)
j = 0
if num == 1:
    print("0")
else:
    for i in range(1, num):
        j = j + int(arglist[i])
    print("{}".format((j)))
