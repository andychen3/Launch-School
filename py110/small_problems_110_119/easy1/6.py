# https://launchschool.com/exercises/0871b97b

'''
Questions:
1. Do numbers count as a word?
2. Do i need to cehck for invalid string input

Input: String consisting of zero or more space separated words
Output: dictionary that shows number of words of different sizes
Explicit: string can contain zero or more space separated words
answered - words consist of any sequence of non-space characters
excludes non-letters.
Implicit:
1. empty string = empty dictionary
3. multiple words can share the same length


Pseudocode:
1. Break string into a list of words
2. Iterate through each word and count the number of characters
3. Store number of characters into dictionary
4. Return dictionary

'''
def count_word(word):
    '''
    Count number of characters in a word exlcluding non-letters
    '''
    count = 0

    for char in word:
        if char.isalpha():
            count += 1
    return count


def word_sizes(sentence):
    words = sentence.split()
    num_of_words = {}

    for word in words:
        length = count_word(word)
        num_of_words.setdefault(length, 0)
        num_of_words[length] += 1
    
    return num_of_words

# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})




