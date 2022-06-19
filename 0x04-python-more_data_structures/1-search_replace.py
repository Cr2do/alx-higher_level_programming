#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for (k, i) in enumerate(my_list):
        if i == search:
            my_list[k] = replace
    return my_list
