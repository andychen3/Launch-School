"""

input: string
output: Boolean if the string is a pangram
rules:

Algorithm:


"""

def is_pangram(my_str):
    freq_dict = {}

    for char in my_str.lower():
        if char.isalpha():
            if char not in freq_dict:
                freq_dict[char] = 0
            freq_dict[char] += 1
    
    return len(freq_dict) == 26

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)