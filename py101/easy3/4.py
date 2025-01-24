# https://launchschool.com/exercises/b7b7220a

def stringy(num):
    string = []

    for i in range(num):
        if i % 2 == 0:
            string.append("1")
        else:
            string.append("0")
    return "".join(string)


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True