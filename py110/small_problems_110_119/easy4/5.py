# https://launchschool.com/exercises/b00376c3

def unique_from_first(lst1, lst2):
    return set(lst1) - set(lst2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})