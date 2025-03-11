# https://launchschool.com/exercises/f62ab8aa

"""

input: list
output: return the list sorted in ascending order
rules:
1. Same data type for the lists that are passed in


1 2 3 4

[1, 2] [3, 4] 

Algo:


"""

def merge(lst1, lst2):
    result = []
    index1 = 0
    index2 = 0

    while index1 < len(lst1) and index2 < len(lst2):
        num1 = lst1[index1]
        num2 = lst2[index2]

        if num1 <= num2:
            result.append(num1)
            index1 += 1
        else:
            result.append(num2)
            index2 += 1
            
    if index1 < len(lst1):
        result.extend(lst1[index1:])
        # while index1 < len(lst1):
        #     result.append(lst1[index1])
        #     index1 += 1

    if index2 < len(lst2):
        result.extend(lst2[index2:])
        # while index2 < len(lst2):
        #     result.append(lst2[index2])
        #     index2 += 1
    
    return result


def merge_sort(lst):
    mid = len(lst) // 2
    if len(lst) == 1:
        return lst
    
    sub_list1 = merge_sort(lst[:mid])
    sub_list2 = merge_sort(lst[mid:])
    
    return merge(sub_list1, sub_list2)

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)