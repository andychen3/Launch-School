# Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.


# print(most_common_char('Hello World') == 'l')
# print(most_common_char('Mississippi') == 'i')
# print(most_common_char('Happy birthday!') == 'h')
# print(most_common_char('aaaaaAAAA') == 'a')

# my_str = 'Peter Piper picked a peck of pickled peppers.'
# print(most_common_char(my_str) == 'p')

# my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
# print(most_common_char(my_str) == 'e')

'''
Q'
1. Do i have to account for empty strings?
2. Wat about puncutations?

input: string 
output: returns char that occurs most often
rule:
1. if there are multiple chars with the same greatest freq return the one
that appears first in the string. 
2. when counting chars consider uppercase and lowercase versions to be the same


algorithm:
1. Create empty dictionary
2. Iterate through each character and add it to the empty dictionary
3. lowercase the character and check if its in dictionary
4. if not create an entry and add it
5. find the max value of the values
6. iterate through the dictionary and match it with the max value and return the key

'''

def most_common_char(string):
    freq_dict = {}

    for char in string.lower():
        if char not in freq_dict:
            freq_dict[char] = 0
        
        freq_dict[char] += 1

    max_value = max(freq_dict.values())
    
    for key, value in freq_dict.items():
        if value == max_value:
            return key

    

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')