# Name: Andy Chen
# Description: PY101 - PY109 Small Problems Easy 1

# 1
# Write a function that takes one integer argument and returns True
# when the number's absolute value is odd, False otherwise.
# def is_it_odd(number):
#     if abs(number) % 2 != 0:
#         return True
#     return False

# print(is_it_odd(1)) # True
# print(is_it_odd(2)) # False
# print(is_it_odd(-1)) # True

# 2
# Print all odd numbers from 1 to 99, inclusive, 
# with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating over 
# just the odd numbers?

# for num in range(1, 100):
#     if num % 2 != 0:
#         print(num)

# for num in range(1, 100, 2):
#     print(num)

# 3
# Print all even numbers from 1 to 99, inclusive, 
# with each number on a separate line.
# Bonus Question: Can you solve the problem by iterating
# over just the even numbers?

# for num in range(1, 100):
#     if num % 2 == 0:
#         print(num)

# for num in range(2, 100, 2):
#     print(num)


# 4
# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.
# Note: 1 square meter == 10.7639 square feet

# while True:
#     length = int(input("Please enter the length. "))
#     width = int(input("Please enter the width. "))

#     area_in_meters = length * width
#     area_in_feet = length * width * 10.7639
#     print(f"Here is the area of your room in meters {area_in_meters:.2f} and in square feet {area_in_feet:.2f}.")



# 5 
# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. 
# The program must compute the tip, then print both the tip and the total amount of the bill. 
# You can ignore input validation and assume that the user will enter valid numbers.

# while True:
#     bill = float(input("What is the bill? "))
#     tip = float(input("What is the tip percentage? "))

#     tip_amount = bill * (tip / 100)
#     total = bill + tip_amount
    
#     print(f"The tip is ${tip_amount:.2f}")
#     print(f"The total is ${total:.2f}")



# 6
# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of all numbers 
# between 1 and the entered integer, inclusive.
# add validation


# while True:
#     number = int(input("Please enter an integer greater than 0: "))

#     choice = input("Enter 's' to compute the sum, or 'p' to compute the product. ")

#     if choice == "s":
#         total = 0
#         for num in range(1, number + 1):
#             total += num
#         print(f"The sum of the integers between 1 and {number} is {total}.")
#     elif choice == "p":
#         product = 1
#         for num in range(1, number + 1):
#             product *= num
#         print(f"The product of the integers between 1 and {number} is {product}.")
#     else:
#         raise ValueError("Please enter 's' or 'p'.")


# 7
# Write a function that takes two strings as arguments, determines the length of the two strings,
#  and then returns the result of concatenating the shorter string, the longer string, 
# and the shorter string once again. You may assume that the strings are of different lengths.
# def short_long_short(string1, string2):
#     short = None
#     long = None

#     if len(string1) < len(string2):
#         short = string1
#         long = string2
#     elif len(string1) > len(string2):
#         long = string1
#         short = string2
    
#     return short + long + short


# # These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")


# 8
# Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.

# For simplicity, this exercise assumes that the Gregorian calendar has been in continuous use since the year 1. We'll address that assumption in the next exercise that follows this one.

# To determine whether a given year is a leap year, use the rules of the Gregorian calendar:

# If the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

# def is_leap_year(year):
#     if year % 400:
#         return True
#     elif year % 100:
#         return False
#     else:
#         return year % 4 == 0

# # # These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == False)
# print(is_leap_year(1100) == False)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == False)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)



# 9
# def is_leap_year(year):
    #   if year < 1752 and year % 4 == 0:
    #     return True
#     elif year % 400:
#         return True
#     elif year % 100:
#         return False
#     else:
#         return year % 4 == 0

# # # These examples should all print True
# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# 10
# Write a function that computes the sum of all numbers between 1 and some other number, 
# inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, 
# the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).
# You may assume that the number passed in is an integer greater than 1.

# def multisum(number):
#     total = 0

#     for num in range(1, number + 1):
#         if num % 3 == 0 or num % 5 == 0:
#             total += num
#     return total

# # These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)


# 11
# Write a function that determines and returns the UTF-16 string value of a string
#  passed in as an argument. The UTF-16 string value is the sum of the UTF-16 values of 
# every character in the string. (You may use ord to determine the UTF-16 value of a character.)

# def utf16_value(string):
#     total = 0

#     for char in string:
#         total += ord(char)
#     return total

# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)