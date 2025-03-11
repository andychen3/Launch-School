# https://launchschool.com/exercises/69f60f05

'''

input: string
output: string with replaced string values as number
rule:

'''

def word_to_digit(message):
    number_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    new_message = []

    for word in message.split():
        if word in number_dict:
            new_message.append(number_dict[word])
        else:
            new_message.append(word)

    return " ".join(new_message)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True