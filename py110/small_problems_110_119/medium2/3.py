# https://launchschool.com/exercises/5fa18f7b

'''

input:
output:
rules:

Invalid:
1. sum all degrees and if it is not 180 return invalid
2. sort list and check the first element if it is less than or equal to 0

3 right, acute, obtuse
sort the list and check the end. if it is greater than 90 return obtuse
if it is less than 90 return acute
and if it is 90 then return right
'''

def triangle(side1, side2, side3):
    triangle_list = sorted([side1, side2, side3])
    
    if sum(triangle_list) != 180 or triangle_list[0] <= 0:
        return "invalid"
    elif triangle_list[-1] > 90:
        return "obtuse"
    elif triangle_list[-1] < 90:
        return "acute"
    else:
        return "right"
    
print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True