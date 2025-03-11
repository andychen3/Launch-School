# https://launchschool.com/exercises/5c5d7f1f

def staggered_case(string):
    return "".join([char.upper() if idx % 2 == 0 else char.lower() 
                    for idx, char in enumerate(string)])

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True



# def staggered_case(string):
#     new_string = []

#     for idx, char in enumerate(string):
#         if char.isalpha():
#             if idx % 2 == 0:
#                 new_string.append(char.upper())
#             else:
#                 new_string.append(char.lower())
#         else:
#             new_string.append(char)
        
#     return "".join(new_string)


# def staggered_case(string):
#     new_string = []

#     for idx, char in enumerate(string):
#         new_char = char.upper() if idx % 2 == 0 else char.lower()
#         new_string.append(new_char)
        
#     return "".join(new_string)