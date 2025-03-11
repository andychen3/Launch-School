# https://launchschool.com/exercises/2c5c3272

'''

input: 3 numeric inputs
output: a string. 4 options
rules:

# sort and sum the first two elements and if it is less then the third reutnr false
# check first element. if its 0 return

# if i set it and its empty equilateral
# if its length of 1 then its isosceles
# if its length of 2 then its scalene


Algorithm:

'''

def triangle(side1, side2, side3):
    sorted_sides = sorted([side1, side2, side3])

    if sorted_sides[0] <= 0:
        return "invalid"
    
    if sum(sorted_sides[:2]) <= sorted_sides[2]:
        return "invalid"
    
    triangle_set = set(sorted_sides)
    length = len(triangle_set)

    if length == 1:
        return "equilateral"
    elif length == 2:
        return "isosceles"
    else:
        return "scalene"

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True
