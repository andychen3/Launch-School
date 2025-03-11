# https://launchschool.com/exercises/17162736?track=python
"""
input: fraction
output:
rules:
1st function takes a rational number as an argument and returns a list of denominators

2nd function takes the list of numbers in that format and returns a rational number

2




Algo:

"""

from fractions import Fraction

def egyptian(real_number):
    denominator = []
    potential_denominator = 1
    target = real_number
    while target != 0:
        unit_fraction = Fraction(1, potential_denominator)
        if unit_fraction <= target:
            target -= unit_fraction
            denominator.append(potential_denominator)
        potential_denominator += 1
    
    return denominator

def unegyptian(lst):
    return sum([Fraction(1, d) for d in lst])

print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))

print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))






