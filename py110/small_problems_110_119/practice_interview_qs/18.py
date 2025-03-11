"""

input: list of integers
output: integer index N which all numbers with an index less than N
sum to the same value as the numbers with an index greater then N.
If no index return -1
rules:
1. If given a list with multiple answers return with the smallest value
2. sum of the numbers to the left of index 0 is 0
3. sum of the numbers to the right of last element is 0

0 1 2 3 4 5 6
1 2 4 4 2 3 2

0 1 2
1 2 3

left_sum = 3
right_sum = 3

1


1 3 6




Algorithm:
1. left_sum = 0
2. Get the total of the right by summing all the numbers
3. Itereate trhough each number. 
4. First check if left_sum = right_sum: if it is return index
5. add current number to left_sum
6. subtract out current number from right_sum
7 return -1

"""

# def equal_sum_index(lst):
#     left_sum = 0
#     total_sum = sum(lst)

#     for index, num in enumerate(lst):
#         right_sum = total_sum - left_sum - num
        
#         if left_sum == right_sum:
#             return index
#         left_sum += num
        

#     return -1

def equal_sum_index(lst):
    left_sum = 0
    right_sum = sum(lst)

    for index, num in enumerate(lst):
        right_sum -= num
        
        if left_sum == right_sum:
            return index
        left_sum += num
        

    return -1


print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)
print(equal_sum_index([1]) == 0)