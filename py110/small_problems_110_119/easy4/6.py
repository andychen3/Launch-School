# https://launchschool.com/exercises/e01f3df2

def leading_substrings(string):
    return [string[:idx + 1] for idx in range(len(string))]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])


# def leading_substrings(string):
#     result = []
#     substring = ""

#     for char in string:
#         substring += char
#         result.append(substring)
    
#     return result