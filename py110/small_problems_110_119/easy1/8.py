# https://launchschool.com/exercises/097dfb47

'''
Questions:
1. Standard conversion do you mean can't use float?
2. Am i able to use ord and chr?

Input: string of digits
Output: integer 
Explicit:
1. Not worry about + or -
2. No invalid characters
3. Cannot use int
Implicit:


Pseudocode:
1. Create an empty list
2. Iterate through the string
3. Convert the string to its ascii representation
4. convert ascii representation to its numeric representation
5. Append to list
6. Send that list to a function that finds the digit
7. find the length of each digit's place by subtracting index from total length
and multiply by the length * 10. If its length 1 add the last index and break
8. return converted digit

'''
def convert_to_int(digit_list):
    result = 0
    length = len(digit_list) - 1

    for index, num in enumerate(digit_list):
        result += 10 ** (length - index) * num
    
    return result

def string_to_integer(string): 
    return convert_to_int([ord(digit) - 48 for digit in string])

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True