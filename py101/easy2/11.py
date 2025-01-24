# https://launchschool.com/exercises/9c9b5055

def center_of(string):
    length = len(string)
    middle = length // 2

    if length % 2 == 0:
        return string[middle - 1: middle + 1]
    else:
        return string[middle]


print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True