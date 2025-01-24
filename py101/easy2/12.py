# https://launchschool.com/exercises/9f1d2e9c

def negative(num):
    return num if num < 0 else num * -1

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True