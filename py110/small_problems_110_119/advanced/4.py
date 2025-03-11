# https://launchschool.com/exercises/64bea0a1

"""
Q:
1. 

input: two sorted lists
output: list that contains all elements from both list in ascending sorted order
rules:
1. Contain either all integer or string values
2. Cannot sort the result list
3. You must build the list one element at a time
4. should not mutate the input lists
5. Empty list does not matter it will return the other list



2 6 

1 2 5 6 9
while loop


Algo:
1. Create empty list
2. While loop to iterate between both lists. Condition is based on
whether or not there is still elelemtsn in the list(while list1 has elements and
list2 has elements)
    2a. compare the two elements and whichever is less append it first
    2b. append the second element
3. check if list1 still has elements add the rest
4. check if list2 still has elements add the rest
5. return the list


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

    if index2 < len(lst2):
        result.extend(lst2[index2:])
    
    return result

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)