# https://launchschool.com/exercises/b5a6df28?track=python

def fibonacci(n):
    if n <= 2:
        return 1
    
    first = 1
    last = 1

    for _ in range(2, n):
        new_first = last
        last = first + last
        first = new_first
    return last


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True