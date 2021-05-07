#!/usr/bin/python
def search_replace(my_list, search, replace):
    #lambda retorna replace si x=search sino el mismo x 
    my_list = list(map(lambda x: replace if x == search else x, my_list))
    return (my_list)
