# https://launchschool.com/exercises/9e3d8de3

'''
input: number
output: boolean
rules:
1. can't use other methods
2. Determine if a number is prime.


if number 1 return False
if number 2 return True


'''
def is_prime(number):
    if number == 1:
        return False
    
    number_of_divisibility = 0

    for num in range(2, number + 1):
        if number % num == 0:
            number_of_divisibility += 1
        if number_of_divisibility > 2:
            return False
        
    return True

print(is_prime(999_998_727_899_993) == False)              # True
# print(is_prime(2) == True)               # True
# print(is_prime(3) == True)               # True
# print(is_prime(4) == False)              # True
# print(is_prime(5) == True)               # True
# print(is_prime(6) == False)              # True
# print(is_prime(7) == True)               # True
# print(is_prime(8) == False)              # True
# print(is_prime(9) == False)              # True
# print(is_prime(10) == False)             # True
# print(is_prime(23) == True)              # True
# print(is_prime(24) == False)             # True
# print(is_prime(997) == True)             # True
# print(is_prime(998) == False)            # True
# print(is_prime(3_297_061) == True)       # True
# print(is_prime(23_297_061) == False)     # True