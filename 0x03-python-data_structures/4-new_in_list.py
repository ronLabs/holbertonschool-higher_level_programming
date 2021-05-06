#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0):
        return (my_list)
    elif (idx > len(my_list) - 1):
        return (my_list)
    else:
        list_copy = my_list.copy()
        list_copy[idx] = element
        return (list_copy)
