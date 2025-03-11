# https://launchschool.com/exercises/97414944
"""

input: sorted list, item to be found
output: index of found element or -1 if not found
rules:


Algo:
1. left = 0 and a right = len(list) - 1
2. while left < right:
3. find the mid index. and then check if mid index element is your answer if so return mid
4. if not then you compare if the number is greater then the mid. 
5. if it is then you make right = to mid + 1
6. else if the number is less then the mid then left = mid - 1
7 return -1

"""

'''

3
l = 2
r = 2

m = (2 + 2) // 2 = 2

012
123

'''

def binary_search(lst, item):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == item:
            return mid
        if item > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1            
    return -1

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)