#!/usr/bin/python3
isUpper = True
for i in range(122, 96, -1):
    if(isUpper):
        print("{}".format(chr(i).lower()), end="")
        isUpper = False
    else:
        print("{}".format(chr(i).upper()), end="")
        isUpper = True
