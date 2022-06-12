#!/usr/bin/python3
from operator import indexOf
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
    elif len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        print("{} argument:".format(len(sys.argv) - 1))
    for i in sys.argv:
        if(i != sys.argv[0]):
            print("{}: {}".format(indexOf(sys.argv, i), i))
