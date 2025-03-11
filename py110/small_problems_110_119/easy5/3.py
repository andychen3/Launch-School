# https://launchschool.com/exercises/bb9d55f5

def vowels_removed(string):
    new_string = []
    
    for char in string:
        if char.lower() not in "aeiou":
            new_string.append(char)
    
    return "".join(new_string)


def remove_vowels(list_of_strings):
    result = []

    for string in list_of_strings:
        result.append(vowels_removed(string))

    return result

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True
    


