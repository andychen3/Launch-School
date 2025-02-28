# https://launchschool.com/exercises/39d24ce3


def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

def substrings(string):
    substring_list = [leading_substrings(string[idx:]) for idx in range(len(string))]
    combined_list = []

    for substrings in substring_list:
        combined_list.extend(substrings)
    
    return combined_list


expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True


# def leading_substrings(string):
#     return [string[:idx + 1] for idx in range(len(string))]

# def substrings(string):
#     substring_list = [leading_substrings(string[idx:]) for idx in range(len(string))]
#     combined_list = []

#     for substrings in substring_list:
#         combined_list.extend(substrings)
    
#     return combined_list



# another solution

# def substrings(string):
#     result = []

#     for idx, char in enumerate(string):
#         substring = []
#         for i in range(idx, len(string)):
#             substring.append(string[i])
#             result.append("".join(substring))
#     return result
