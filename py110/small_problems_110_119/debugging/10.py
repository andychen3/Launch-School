# https://launchschool.com/exercises/9c0dec0a

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]

unique_data = list(dict.fromkeys(data))

# freq_dict = {}

# for num in data:
#     if num not in freq_dict:
#         freq_dict[num] = 1

# unique_data = list(freq_dict)


print(unique_data == [4, 2, 1, 3]) # order not guaranteed