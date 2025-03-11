"""
1. identical pair

input: list of integers
output: integer of identical pairs
rules:
1. if list is empty or contains exactly one value return 0
2. certain numbers occur more than twice but count each complete pair once.
ex. [1,1,1,1] = 2 [2,2,2,2,2] = 2

Data strucutre - dictionary




Algorithm:
1. if list is empty or len of one return 0
2. create empty freq dict
3. Itereate through the numbers and add the count to the freq dict
3a. pairs = 0
4. iterate through the values and integer divison each of the values by 2 and 
then add it to the count
5. return the count

"""

def pairs(lst):
    if not lst or len(lst) == 1:
        return 0
    
    freq_dict = {}

    for num in lst:
        if num not in freq_dict:
            freq_dict[num] = 0
        freq_dict[num] += 1

    num_of_pairs = 0
    for freq in freq_dict.values():
        num_of_pairs += freq // 2
    
    return num_of_pairs

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)