"""

input: string 
output: copy of string with 
rules:
1. every second character in every third word converted
to uppercase.



Algorithm:
1. Split the string into a list
2. Iterate through the list of words
3. If the index mod 3 is == to 0. That means i am on the third word
4. use another function to count the characters. 
    4a. if len(1) return
    4a. new_string to empty list
    4b. iterate through the list and when i get to index 1 change it to upper
    4c. break

"""

# var = "ase"
# new_var = var[:1] + var[1].upper() + var[2:]
# print(new_var)

def convert_second_letter_to_upper(word):
    if len(word) == 1:
        return word
    
    new_string = []

    for index, char in enumerate(word):
        if index % 2 != 0:
            new_string.append(char.upper())
        else:
            new_string.append(char)
    
    return "".join(new_string)

def to_weird_case(string):
    split_string = string.split()
    result = []
    count_of_words = 1

    for word in split_string:
        if count_of_words % 3 == 0:
            result.append(convert_second_letter_to_upper(word))
        else:
            result.append(word)
        count_of_words += 1
    
    return " ".join(result)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

