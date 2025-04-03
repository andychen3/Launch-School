# https://launchschool.com/exercises/f9ddd613

from functools import reduce

products = reduce(lambda n, accum: accum * n, [1, 2, 3])
print(products)