#!/usr/bin/python3
"""Module for Mylist class."""


class Mylist(list):
    """custom Mylist class."""
    def print_sorted(self):
        """Method to print sorted List."""
        print(sorted(self))
