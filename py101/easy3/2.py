# https://launchschool.com/exercises/34b12905


def crunch(string):
    new_word = []

    for char in string:
        if len(new_word) == 0:
            new_word.append(char)
        elif char != new_word[-1]:
            new_word.append(char)
    return "".join(new_word)


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')