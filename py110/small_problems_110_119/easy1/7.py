# https://launchschool.com/exercises/81a9b8ef

'''
Questions:
1. Can it contain numbers?
2. Do i need to check for invalid input

Input: string of words separated by spaces
Output: string of words with the first and last letter swapped
Explicit:
1. every word contains at least one letter
2. string will always contain at least one word
3. String contains nothing but words and spaces
4. No leading, trailing, or repeated spaces
Implicit:
1. single word returns itself
2. case does not matter.


Pseudocode:
0. Check if length of string is 1. automatically return itself
1. break the string into a list of words
2. set result to an empty list
3. iterate through list of words
4. for each word switch the first and last character
    4a. check if the string is length of one if so return itself
5. append the changed word to the empty list
6. return result joined back into a string 

'''
def switch_first_and_last_char(word):
    '''
    Takes in a word and transform it by switching first and last character
    '''
    if len(word) == 1:
        return word
    
    list_of_char = list(word)
    list_of_char[0], list_of_char[-1] = list_of_char[-1], list_of_char[0]

    return "".join(list_of_char)


def swap(string):
    if len(string) == 1:
        return string
    
    list_of_words = string.split()
    result = []

    for word in list_of_words:
        result.append(switch_first_and_last_char(word))

    return " ".join(result)

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True