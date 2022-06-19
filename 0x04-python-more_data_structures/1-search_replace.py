#!/usr/bin/python3
def search_replace(my_list, search, replace):
    second_list = []
    for el in my_list:
        second_list.append(el)
    for (k, i) in enumerate(second_list):
        if i == search:
            second_list[k] = replace
    return second_list
