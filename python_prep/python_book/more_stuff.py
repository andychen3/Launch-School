# Problems
# Python Book More stuff questions

# 1
# What does the following function do? Be sure to identify the output value.
# def do_something(dictionary):
#     return sorted(dictionary.keys())[1].upper()

# my_dict = {
#     'Karl':     108,
#     'Clare':    175,
#     'Karis':    140,
#     'Trevor':   180,
#     'Antonina': 132,
#     'Chris':    101,
# }

# print(do_something(my_dict))

# It sorts all the keys in lexicographical order and then look for the name in index 
# 1 of the return sorted list and calls upper on it which capitalizes it.
# "CHRIS"


# 2
# Use the sqrt function from the math library to write some code 
# that outputs the square root of 37. Try to write the code in three different 
# ways.
# import math
# print(math.sqrt(37))

# import math as mt
# print(mt.sqrt(37))

# from math import sqrt
# print(sqrt(37))

# 3
# Write a nested function in sum_of_squares 
# that will make this code work as shown.

# def sum_of_squares(num1, num2):
#     def square(num):
#         return num * num

#     return square(num1) + square(num2)

# print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
# print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)


# 4
# Write a function called increment_counter that increments a 
# counter variable every time it is called. You can test your code with 
# the following:

# counter = 0
# def increment_counter():
#     global counter
#     counter += 1


# print(counter)                # 0

# increment_counter()
# print(counter)                # 1

# increment_counter()
# print(counter)                # 2

# counter = 100
# increment_counter()
# print(counter)                # 101


# # 5 

# On reflection, we've decided that we don't want to rely on using a 
# global variable in the code we wrote in the previous example. 
# To fix this, we're going to nest the code from the previous example 
# into an outer function:

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()