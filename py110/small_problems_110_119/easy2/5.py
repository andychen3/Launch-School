# https://launchschool.com/exercises/513e4379

'''
Questions:


Input: 2 lists
Output: 1 list that contains all elements from both list
Explicit:
1. Non empty lists
2. Same number of elements
Implicit:


Pseudocode:

'''
def interleave(lst1, lst2):
    result = []

    for tup in zip(lst1, lst2):
        result.extend(list(tup))
    
    return result


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

