# https://launchschool.com/exercises/f3e4807c

from functools import reduce

single_string = reduce(lambda str1, accum: str1 + accum, ["Launch", " ", "School", " ", "is", " ", "great"])
print(single_string)