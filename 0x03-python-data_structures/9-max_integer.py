#!/usr/bin/python3


def max_integer(my_list=[]):

    if not my_list:
        return None

    j = my_list[0]
    for i in range(0, len(my_list)):
        if j < my_list[i]:
            j = my_list[i]
    return j 
