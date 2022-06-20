#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    return_val = 0
    for (k, v) in enumerate(my_list):
        if k < x:
            print("{}".format(v), end="")
            return_val = return_val + 1
    print("")
    return x if return_val == x else return_val
