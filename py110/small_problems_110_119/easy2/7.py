# https://launchschool.com/exercises/fc642f09

'''
Questions:


Input:
Output:
Explicit:
Implicit:


Pseudocode:

'''

def multiply_list(lst1, lst2):
    return [elem1 * elem2 for elem1, elem2 in zip(lst1, lst2)]

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True