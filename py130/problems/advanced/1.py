# https://launchschool.com/exercise_sets/37acdd95

"""
input: string of texts
output: None. printing longest sentence and how many words in longest
rules:
1. End of sentences can be ".", "!", "?"
2. Any other chars are words. 

DS:



Algo:
3 different list split based on end
Find max of each non empty list
append the appropriate ending to the max found
compare the 3 maxes from each list to find the longest
Print out longest
Print out sentence that has the length of the longest sentence

"""

def longest_sentence(string):
    list_of_words = string.split()
    longest_length_sentence = None
    building_sentence = []

    for word in list_of_words:
        if word.endswith((".", "?", "!")):
            building_sentence.append(word)
            length = len(building_sentence)
            sentence = " ".join(building_sentence)

            if longest_length_sentence is None:
                longest_length_sentence = (sentence, length)
            elif length > longest_length_sentence[1]:
                longest_length_sentence = (sentence, length)
                
            building_sentence = []
            continue
        
        building_sentence.append(word)

    print(f"longest_length_sentence[0]\n")
    print(f"The longest sentence has {longest_length_sentence[1]} words.\n")


long_text = (
    'Four score and seven years ago our fathers brought forth on this '
    'continent a new nation, conceived in liberty, and dedicated to the '
    'proposition that all men are created equal. Now we are engaged in a '
    'great civil war, testing whether that nation, or any nation so '
    'conceived and so dedicated, can long endure. We are met on a great '
    'battlefield of that war. We have come to dedicate a portion of that '
    'field, as a final resting place for those who here gave their lives '
    'that that nation might live. It is altogether fitting and proper that '
    'we should do this.'
)

longer_text = long_text + (
    'But, in a larger sense, we can not dedicate, we can not consecrate, '
    'we can not hallow this ground. The brave men, living and dead, who '
    'struggled here, have consecrated it, far above our poor power to add '
    'or detract. The world will little note, nor long remember what we say '
    'here but it can never forget what they did here. It is for us the '
    'living, rather, to be dedicated here to the unfinished work which '
    'they who fought here have thus far so nobly advanced. It is rather '
    'for us to be here dedicated to the great task remaining before us -- '
    'that from these honored dead we take increased devotion to that '
    'cause for which they gave the last full measure of devotion -- that '
    'we here highly resolve that these dead shall not have died in vain '
    '-- that this nation, under God, shall have a new birth of freedom -- '
    'and that government of the people, by the people, for the people, '
    'shall not perish from the earth.'
)

longest_sentence(long_text)
# Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal.
#
# The longest sentence has 30 words.

longest_sentence(longer_text)
# It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
#
# The longest sentence has 86 words.

longest_sentence("Where do you think you're going? What's up, Doc?")
# Where do you think you're going?
#
# The longest sentence has 6 words.

longest_sentence("To be or not to be! Is that the question?")
# To be or not to be!
#
# The longest sentence has 6 words.