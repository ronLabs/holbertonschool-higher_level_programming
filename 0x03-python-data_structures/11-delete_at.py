#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    index = 0

    if idx < 0:
        return my_list

    if (len(my_list)) == 0:
        return my_list

    for elements in my_list[:]:
        if idx == index:
            del(my_list[index])
            return(my_list)
        index += 1

    if idx >= index:
        return my_list
