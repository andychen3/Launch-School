# https://launchschool.com/exercises/bc977f27

'''
Questions:


Input:
Output:
Explicit:
Implicit:


Pseudocode:

'''


# def palindromes(string):
print("13" > "23")


"""
// You will be given a number and you will need to return it as a string in expanded form. For example:

input: integer
output: string representation of the number
Assume input valid number. one argument. Positive number. Incase of 0 it would be an empty string

Data Structures:
1. Convert input into a string or a list of characters


12
0 1

length = 2 - 1

(1 * 10 * 1 - 0) + (2 * 10 * 1 - 1) 

70304
0 1 2 3 4
length = 5 - 1

(7 * 10 ^ (4 - 0)) + (0) + (3 * 10 ^ 2) + 0 + (4 * 10 ^ 4 -4)


// expanded_form(12); # Should return '10 + 2'
// expanded_form(42); # Should return '40 + 2'
// expanded_form(70304); # Should return '70000 + 300 + 4'

// Note: All numbers will be whole numbers greater than 0.

// p expanded_form(12) == '10 + 2'
// p expanded_form(42) == '40 + 2'
// p expanded_form(70304) == '70000 + 300 + 4'

// print(expanded_form(12) == '10 + 2')
// print(expanded_form(42) == '40 + 2')
// print(expanded_form(70304) == '70000 + 300 + 4')

// console.log(expanded_form(12) == '10 + 2');
// console.log(expanded_form(42) == '40 + 2');
// console.log(expanded_form(70304) == '70000 + 300 + 4');

Pseudocode:
1. Convert input into a string
2. Iterate through the string number
3. Find the length of the list
4. Calculate the place of the number
5. join back the string and conver it to a number

"""
def expanded_form(number):
    str_num = str(number)
    result = []
    length = len(str_num) - 1

    for idx, digit in enumerate(str_num):
        num = (int(digit) * (10 ** (length - idx)))
        if num != 0:
            result.append(str(num))


    return " + ".join(result)

print(expanded_form(12) == '10 + 2')
print(expanded_form(42) == '40 + 2')
print(expanded_form(70304) == '70000 + 300 + 4')
