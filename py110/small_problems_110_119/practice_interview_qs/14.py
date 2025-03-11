"""

input: integer
output: returns the sum of all the multiples of 7 and 11 that are less than
the argument
rules:

Algorithm:


"""


def seven_eleven(num):
    if num <= 0:
        return 0
    
    sum_ = 0

    for number in range(num):
        if number % 7 == 0 and number % 11 == 0:
            sum_ += number
        elif number % 7 == 0:
            sum_ += number
        elif number % 11 == 0:
            sum_ += number

    return sum_

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)