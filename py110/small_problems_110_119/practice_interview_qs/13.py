"""

input: two strings
output: Boolean if some portion of the characters in the first string
can be rearragned to match the characters in the second
rules:
1. lowercase
2. no empty string


Algorithm:


"""
def unscramble(str1, str2):
    freq_dict = {}

    for char in str1:
        if char not in freq_dict:
            freq_dict[char] = 0
        freq_dict[char] += 1
    
    for char in str2:
        if char not in freq_dict:
            return False
        freq_dict[char] -= 1
        if freq_dict[char] == 0:
            del freq_dict[char]
    
    return True
print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)