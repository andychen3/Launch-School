# https://launchschool.com/exercises/2d53b50f


def xor(arg1, arg2):
    if arg1 and not arg2:
        return True
    elif arg2 and not arg1:
        return True
    else:
        return False



print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)