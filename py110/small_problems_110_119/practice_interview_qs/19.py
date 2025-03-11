"""

input: list of integers
output: integer that appears an odd number of times
rules:
1. There will always be one such integer in the input list

Algorithm:


"""

def odd_fellow(lst):
    freq_dict = {}

    for num in lst:
        if num not in freq_dict:
            freq_dict[num] = 0
        freq_dict[num] += 1

    for key, freq in freq_dict.items():
        if freq % 2 != 0:
            return key
        
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)