# https://launchschool.com/exercises/8bee659d

'''
Questions:


Input: list of numbers
Output: sum of the sum of leading subsequences (integer)
Explicit:
Implicit:

3, 5, 2

3
3 + 5
3 + 5 + 2


Pseudocode:

'''



def sum_of_sums(num_list):
    running_total = 0
    cummulative_sum = 0

    for num in num_list:
        cummulative_sum += num
        running_total += cummulative_sum
    
    return running_total

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True



# def sum_of_sums(num_list):
#     total = 0

#     for idx in range(len(num_list)):
#         total += sum(num_list[:idx + 1])
    
#     return total