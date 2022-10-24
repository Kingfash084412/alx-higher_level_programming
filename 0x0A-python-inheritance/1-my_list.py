#!/usr/bin/python3


"""class MyList that inherits from list"""


class MyList(list):

    def print_sorted(self):
        """
        This function prints a list, but sorted in ascending order
        """
        print(sorted(self))
