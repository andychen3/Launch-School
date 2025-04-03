# https://launchschool.com/exercises/4d5ed561

word = "apple"

reverse_order = (char for char in word[::-1])
print(list(reverse_order))


# def reverse(string):
#     for char in reversed(string):
#         yield char


# for char in reverse(word):
#     print(char)