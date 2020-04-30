#!/usr/bin/python3
import sys
arglist = sys.argv
if (len(arglist)) <= 1:
    print("0 arguments")
else:
    if (len(arglist)) == 2:
        print("{:d} argument:".format((len(arglist)) - 1))
    else:
        print("{:d} arguments:".format((len(arglist)) - 1))
for i in range(1, (len(arglist))):
    print("{:d}: {}".format(i, arglist[i]))
