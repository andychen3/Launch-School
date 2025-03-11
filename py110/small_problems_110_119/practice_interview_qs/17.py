"""
1. What is a prime number?

input: list of ints
output: min integer value that can be appened to the list so the sum
of all the elements equal the closet prime number that is greater than
the current sum of numbers.
rules:
1. Find out what number to add to the sum to get to the next prime number
2. Contain at least 2 digits
3. All values are greater then 0
4. There may be mutliple occurence sof the numbers in the list
5. prime number can't be itself

To figure out if its a prime number check if its not odd

5 2 - > 7 and then 11




Algorithm:
1. Find the sum of the list
2. Find the next nearest prime number
    1. start a range from 1 to the square root of the number + 1
    2. divide by the number and if it divides evenly then its not prime
    3. if it can't then we found the number
3. return the number - sum of the list
"""

import math

def nearest_prime_sum(lst):
    sum_ = sum(lst)
    current_num = sum_
    

    while True:
        current_num += 1
        prime = True
        for num in range(2, int(math.sqrt(current_num)) + 1):
            if current_num % num == 0:
                prime = False
                break
        
        if prime:
            break
    
    return current_num - sum_
        
print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)