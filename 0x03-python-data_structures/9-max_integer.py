#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        mval = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > mval:
                mval = my_list[i]
        return 
