# https://launchschool.com/exercises/030ec9a5

memo = {}

def fibonacci(n):
    if n <= 2:
        return 1
    
    if n not in memo:
        memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    
    return memo[n]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True