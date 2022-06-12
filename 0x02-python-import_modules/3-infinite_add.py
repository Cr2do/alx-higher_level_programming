#!/usr/bin/python3
from operator import indexOf
import sys


if __name__ == "__main__":
    val_sum = 0
    for i in sys.argv:
        if(i != sys.argv[0]):
            val_sum += int(i)
    print(val_sum)
