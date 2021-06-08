#!/usr/bin/python3
"""def class object"""


class MyInt(int):
    """create"""

    def __eq__(self, other):
        """builtin"""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Swaps the ne builtin"""
        return int.__eq__(self, other)
