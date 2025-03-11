# https://launchschool.com/exercises/31152e2c

def unique_sequence(lst):
    return [num for idx, num in enumerate(lst) if idx == 0 or lst[idx - 1] != num ]

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4] # added a 6 at the end of the original list
expected = [1, 2, 6, 5, 3, 4]
actual = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True


# def unique_sequence(lst):
#     result = []

#     for idx, num in enumerate(lst):
#         if idx == 0 or result[-1] != num:
#             result.append(num)
    
#     return result

# def unique_sequence(lst):
#     return [num for idx, num in enumerate(lst) if idx == 0 or lst[idx - 1] != num ]