# https://launchschool.com/exercises/2de3afe3

'''
Questions:


Input: string
Output: digit
Explicit:
Implicit:


Pseudocode:

'''

def string_to_signed_integer(string):
    digits = {str(num):num for num in range(10)}
    result = 0
    negative = False

    for char in string:
        if char == "-":
            negative = True
        elif char.isdigit():
            result = (10 * result) + digits[char]
    return result if not negative else -result

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

