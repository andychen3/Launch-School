# https://launchschool.com/exercises/f7b9d1a1


'''
Questions:


Input: list of positive integers
Output: string with value rounded to three decimal places
Explicit:
Implicit:


Pseudocode:
# multiply all the numbers togther
# find length of lst
# divide product by length of list
# round to 3 decimal places
# convert to string and return

'''

def multiplicative_average(lst):
    product = 1
    length = len(lst)

    for num in lst:
        product *= num
    
    return f"{(product / length):.3f}"

# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")
    