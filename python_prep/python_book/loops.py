# Python Book Chapter on Loops

# 1
# The following code causes an infinite loop (a loop that never stops iterating). Why?
# counter = 0

# while counter < 5:
#     print(counter)

# There is no condition to change the counter variable which affects whether or not the 
# while loop will eventually become falsy. As of right now the counter is always true thus
# an infinite loop

# 2
# Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. 
# The updated code should use a for loop to display the future ages.
# Original answer
# age = int(input("How old are you? "))
# print(f'You are {age} years old.')
# years = 0

# for _ in range(4):
#     age += 10
#     years += 10
#     print(f"In {years} years, you will be {age} years old.")

# Better answer  
# age = int(input("How old are you? "))
# print(f'You are {age} years old.')

# for years in range(10, 50, 10):
#     print(f"In {years} years, you will be {age + years} years old.")
    

# 3
# Use a while loop to print the numbers in my_list, one number per line. 
# Then, do the same with a for loop.

# my_list = [6, 3, 0, 11, 20, 4, 17]

# # while loop
# i = 0

# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# # For loop
# for num in my_list:
#     print(num)

# 4
# Use a while loop to print all numbers in my_list with even values, one number per line. 
# Then, print the odd numbers using a ' for' loop.
# my_list = [6, 3, 0, 11, 20, 4, 17]

# # while loop 
# index = 0

# while index < len(my_list):
#     number = my_list[index]
#     if number % 2 == 0:
#         print(number)
#     index += 1


# # For loop

# for num in my_list:
#     if num % 2 != 0:
#         print(num)

# 5 
# Print all of the even numbers in the following list of nested lists. Don't use any while loops.
# my_list = [
#     [1, 3, 6, 11],
#     [4, 2, 4],
#     [9, 17, 16, 0],
# ]

# for outer_list in my_list:
#     for num in outer_list:
#         if num % 2 == 0:
#             print(num)

# 6
# Let's try another variation on the even/odd-numbers theme.
# We'll return to the simpler one-dimensional version of my_list.
#  In this problem, you should write code that creates a new list with one element 
# for each number in my_list. If the original number is an even, then the corresponding element
#  in the new list should contain the string 'even'; otherwise, the element should contain 'odd'.

# my_list = [
#     1, 3, 6, 11,
#     4, 2, 4, 9,
#     17, 16, 0,
# ]

# new_list = []
# for num in my_list:
#     if num % 2 == 0:
#         new_list.append("even")
#     else:
#         new_list.append("odd")
# print(new_list)


# 7
# Write a find_integers function that returns a list of all the integers from my_tuple:

def find_integers(my_tuple):
    return [selection for selection in my_tuple if type(selection) is int]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]



# 8
# Write a comprehension that creates a dict object whose keys are strings and whose values 
# are the length of the corresponding key. Only keys with odd lengths should be in the dict.
#  Use the set given by my_set as the source of strings.

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }

# new_dict = {name: len(name) for name in my_set if len(name) % 2 != 0}
# print(new_dict)


# 9
# Don't let the math scare you. This is a logic and syntax problem, not a math problem.

# Write a function that computes and returns the factorial of a number by 
# using a for or while loop. The factorial of a positive integer n, signified by n!,
#  is defined as the product of all integers between 1 and n, inclusive:

# n!	Expansion	Result
# 1!	1	1
# 2!	1 * 2	2
# 3!	1 * 2 * 3	6
# 4!	1 * 2 * 3 * 4	24
# 5!	1 * 2 * 3 * 4 * 5	120
# You may assume that the argument is always a positive integer.

# def factorial(num):
#     factorial_of_num = 1

#     for num in range(1, num + 1):
#         factorial_of_num *= num
#     return factorial_of_num

# print(factorial(1))   # 1
# print(factorial(2))   # 2
# print(factorial(3))   # 6
# print(factorial(4))   # 24
# print(factorial(5))   # 120
# print(factorial(6))   # 720
# print(factorial(7))   # 5040
# print(factorial(8))   # 40320
# print(factorial(25))  # 15511210043330985984000000


# 10
# The following code uses the randrange function from Python's random 
# library to obtain and print a random integer within a given range. 
# Using a while loop, it keeps running until it finds a random number that matches the 
# last number in the range. Refactor the code so it doesn't require two different invocations 
# of randrange.


# import random

# highest = 10

# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break

# 11
# Print all of the even numbers in the following 
# list of nested lists. This time, don't use any for loops.

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

outer_index = 0


while outer_index < len(my_list):
    inner_index = 0
    while inner_index < len(my_list[outer_index]):
        num = my_list[outer_index][inner_index]
        if num % 2 == 0:
            print(num)
        inner_index += 1
    outer_index += 1


# [print(num) for outer_list in my_list for num in outer_list if num % 2 == 0]

