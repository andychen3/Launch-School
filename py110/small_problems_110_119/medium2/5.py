# https://launchschool.com/exercises/07af1741

"""

input: integer
output: next featured integer or error
rules:
1. output has to be greater then input
2. featured number is odd
3. multiple of 7
4. all digits occcuring exactly once. 123


7 
14
21 
28

12 + 1 
13 + 1 


Algo:
1. 

2. Function to check if number is odd multiple of 7 and occurs exactly once
3. number is odd by % 2 != 0, number % 7, len(set(str)) == len(str)

"""

def check_if_valid_feature(num):
    num += 1
    while num % 7 != 0 or num % 2 == 0:
        num += 1
    
    return num

def check_unique(num):
    while len(set(str(num))) != len(str(num)):
        num += 14
    return num


def next_featured(integer):
    error = ("There is no possible number that "
         "fulfills those requirements.")

    num = integer

    while num < 9876543201:

     
        num = check_if_valid_feature(integer)
        unique_num = check_unique(num)
        return unique_num
    
    
    return error

# print(next_featured(12) == 21)                  # True
# print(next_featured(20) == 21)                  # True
# print(next_featured(21) == 35)                  # True
# print(next_featured(997) == 1029)               # True
# print(next_featured(1029) == 1043)              # True
# print(next_featured(999999) == 1023547)         # True
# print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True
    
    
             
