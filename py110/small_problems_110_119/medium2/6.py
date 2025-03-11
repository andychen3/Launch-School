# https://launchschool.com/exercises/c5b25237

def sum_square_difference(number):
    sum_before_square = 0
    square_by_number = 0

    for num in range(1, number + 1):
        sum_before_square += num
        square_by_number += (num **2)

    return (sum_before_square**2) - square_by_number


print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True