"""

input:
output:
rules:


Algorithms:


"""

def what_is_different(lst):
    freq_dict = {}

    for num in lst:
        if num not in freq_dict:
            freq_dict[num] = 0
        freq_dict[num] += 1

    for key, freq in freq_dict.items():
        if freq == 1:
            return key
        
print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)