# https://launchschool.com/exercises/6c0ff432

'''
Questions:


Input: list
Output: a list that contains two lists
Explicit:
1. first half of the elements in the first list and then the rest in second
2. If list is odd number then the middle element is in first half of the list
Implicit:
1. Empty list? = empty on both
2. if 1 element then one on both and the other is empty

Pseudocode:
# even length of list
# odd length of list
# empty list
# if one element in input list

Create a result that is a list that contains two list
Find the length of the input list
If even:

Else:



'''
def halvsies(lst):
    length = (len(lst) + 1 ) // 2
    first_half = lst[:length]
    second_half = lst[length:]
    return [first_half, second_half]
    

print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])
