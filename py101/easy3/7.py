# https://launchschool.com/exercises/a5d07c11

def twice(number):
    string_number = str(number)
    length = len(string_number)
    middle = length // 2
    
    if length % 2 != 0:
        return number * 2
    if string_number[:middle] == string_number[middle:]:
        return number
    else:
        return number * 2


    


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True