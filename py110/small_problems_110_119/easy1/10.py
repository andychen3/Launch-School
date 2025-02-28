# https://launchschool.com/exercises/6134db97

'''
Questions:


Input: number
Output: string
Explicit:
1. Can't use str
2. Non negative
Implicit:

# 4 -> 52
using chr() to convert a number back to a string

Pseudocode:
Create dictionary of numbers equal to string equivalent


# Get the individual numbers from the whole number
# using a for loop to iterate until the number is 1
# Convert those numbers by adding 48 and then using chr() on it
# Add it to the result list
# join the result list
# return



'''

def integer_to_string(number):
    digits = {num: chr(num + 48) for num in range(10)}
    string_number = []
    input_number = number

    while input_number:
        remainder = input_number % 10
        input_number = input_number // 10
        string_number.append(digits[remainder])
    
    return "".join(string_number[::-1]) or '0'

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True