# Python Book Chapter on Collections

# 1
# Write Python code to print the seventh number of range(0, 25, 3).
list_of_numbers = range(0, 25, 3)
seventh_num = list_of_numbers[6]
print(seventh_num)

# 2
# Use slicing to write Python code to print a 6-character substring of 
# 'Launch School' that begins with the first c.
substring = "Launch School"
start = substring.index("c")
print(substring[start:start + 6])

# 3
# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new 
# tuple should be in reverse order from the original. It should also 
# exclude the first and last members of the original. The result 
# should be the tuple (4, 3, 2).

original_tuple = (1, 2, 3, 4, 5)
my_list = list(original_tuple)
my_list.reverse()
result = tuple(my_list[1:-1])
print(result)

# Using reversed and then converting it to a list and then eventually converting it to a tuple
# uses more memory then just converted it into a list then using reverse method and then slicing
# and converting back to a tuple


# 4
# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.
# Part 2: Write some code to print None when you try to print the value 
# associated with the non-existent key, Lizard.
# Part 3: Write some code to print <silence> when you try to print the value
#  associated with the non-existent key, Lizard.

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets["Dog"])
print(pets.get("Lizard"))
print(pets.get("Lizard", "<silence>"))



# 5 
# Which of the following values can't be used as a key in a dict object, and why?

'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b']
{'a': 1, 'b': 2}
range(5)
{1, 4, 9, 16, 25}
3
0.0
frozenset({1, 4, 9, 16, 25})

# The list ['a', 'b'], {1, 4, 9, 16, 25}, {'a': 1, 'b': 2} cannot be used as a key because it is mutable. The other values are immutable.

# 6
print('abc-def'.isalpha()) # False
print('abc_def'.isalpha()) # False
print('abc def'.isalpha()) # False
print('abc def'.isalpha() and
      'abc def'.isspace()) # False
print('abc def'.isalpha() or
      'abc def'.isspace()) # False
print('abcdef'.isalpha()) # True
print('31415'.isdigit()) # True
print('-31415'.isdigit()) # False
print('31_415'.isdigit()) # False
print('3.1415'.isdigit()) # False
print(''.isspace()) # False


# 7
# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_list = info.split(":")
new_info = "+".join(new_list)
print(new_info)

# Second way to do it
print(info.replace(":", "+"))



# 8
# Explain why the code below prints different values on lines 3 and 4.
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# The codes print different values because the first one takes a slice of the text. For example,
# since it slices the text at index 21 to index 35 the text is actually "for the fjords".
# The length of this string is only  so when you 14.
# do the rfind from this word you u get the first f at fjords which is index 8.
# While for the second one the length of the whole string is 36 and you are looking  starting from the 21st 
# index to the 36 index. And if you go back from there the first f is at the 29th index.


# 9
# Write some code to replace the value 6 in the following nested list with 606:
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][-2] = 606
# stuff[1][3] = 606
print(stuff)


# 10
# Write one line of code to print the activities that Cocoa enjoys.

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats["Pete"]["Cocoa"]["enjoys"])
[print(activities) for activities in cats["Pete"]["Cocoa"]["enjoys"]]



# 11
# Without running the following code, determine what each line should print.

print('johnson' in 'Joe Johnson') # False
print('sen' not in 'Joe Johnson') # True
print('Joe J' in 'Joe Johnson') # True
print(5 in range(5)) # False
print(5 in range(6)) # True
print(5 not in range(5, 10)) # False
print(0 in range(10, 0, -1)) # False
print(4 in {6, 5, 4, 3, 2, 1}) # True
print({1, 2, 3} in {1, 2, 3}) # False
print({3, 2} in {1, frozenset({2, 3})}) # True

# 12
# Write some code that determines and prints whether the number 3 
# appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)          # True
print(3 in numbers2)          # False
print(3 in numbers3)          # False
print(3 in numbers4)          # False (3 != '3')
print(3 in numbers5)          # True  (3 == 3.0)


# 13
# Without running the following code, determine what each print statement should print.
cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats) #True
print('Butter' in cats) # False
print('Butter' in cats[3]) # True
print('cheddar' in cats) # False

# 14
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)


# Write some code that combines the sequences into a list of tuples. 
# Each tuple should contain one member of each sequence. 
# Print the final result so you can see all the values, which should look like this:

print(list(zip(my_str, my_list, my_tuple, my_range)))

# [('a', 'Alpha', None, 10),
#  ('b', 'Bravo', True, 20),
#  ('c', 'Charlie', False, 30)]

# 15
# Without running the following code, what values will be printed by line 10?
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)

# "Cat", "Bird", "Snake"
