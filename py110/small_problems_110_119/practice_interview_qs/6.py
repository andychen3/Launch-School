# Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.


# expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
# print(count_letters('woebegone') == expected)

# expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
#             'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
# print(count_letters('lowercase/uppercase') == expected)

# expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
# print(count_letters('W. E. B. Du Bois') == expected)

# print(count_letters('x') == {'x': 1})
# print(count_letters('') == {})
# print(count_letters('!!!') == {})

"""
1. invalid input?
2. punctuations?
3. uppercase?

input: string
output: dict object in which keys represent lowercase letters in the string values represesnt
 how often the corresponding letters occur in the string
rules:
1. disregard punctuations
2. disregard uppercase
3. empty string is empty dict
4. if only punctuation also empty dict




Algorithm:
1. create freq dict empty
2. itereate through each char and check if it is alpha and lower.
3. check if it is in dict. if not add it
4. return dictionary

"""

def count_letters(string):
    freq_dict = {}

    for char in string:
        if char.isalpha() and char.islower():
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
    return freq_dict
            
expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})
