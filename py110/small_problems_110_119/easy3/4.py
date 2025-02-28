# https://launchschool.com/exercises/157bb2c4

def double_consonants(string):
    result = []

    for char in string:
        if char.lower().isalpha() and char.lower() not in "aeiou":
            result.append(char * 2)
        else:
            result.append(char)

    return "".join(result)

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")