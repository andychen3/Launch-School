# https://launchschool.com/exercises/f2e7ee97

# def clean_up(string):
#     new_string = []

#     for char in string:
#         if char.isalpha():
#             new_string.append(char)
#         elif not new_string and not char.isalpha():
#             new_string.append(" ")
#         elif not char.isalpha() and new_string[-1] == " ":
#             continue
#         elif not char.isalpha() and new_string[-1] != " ":
#             new_string.append(" ")

#     return "".join(new_string)

# print(clean_up("---what's my +*& line?") == " what s my line ")
# # True

def clean_up(string):
    new_string = []

    for char in string:
        if char.isalpha():
            new_string.append(char)
        elif not new_string or new_string[-1] != " ":
            new_string.append(" ")

    return "".join(new_string)

print(clean_up("---what's my +*& line?") == " what s my line ")
# True

