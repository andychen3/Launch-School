# https://launchschool.com/exercises/38a967de

# def oddities(nums):  
#     odd_list = []
#     for index, num in enumerate(nums):
#         if index % 2 == 0:
#             odd_list.append(num)
#     return odd_list

# Bonus question: Try to solve the problem using list slicing.

# def oddities(nums):  
#     return nums[::2]



# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

def evens(nums):  
    return [nums[index] for index in range(len(nums)) if index % 2 != 0]



print(evens([2, 3, 4, 5, 6]) == [3, 5])  # True
print(evens([1, 2, 3, 4]) == [2, 4])        # True
print(evens(["abc", "def"]) == ['def'])     # True
print(evens([123]) == [])                # True
print(evens([]) == [])                      # True