# https://launchschool.com/exercises/bb605dc4

def staggered_case(string):
    result = []
    capitalize = True

    for char in string:
        if char.isalpha():
            new_char = char.upper() if capitalize else char.lower()
            result.append(new_char)
            capitalize = not capitalize
        else:
            result.append(char)
    
    return "".join(result)


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True


# def staggered_case(string):
#     result = []
#     capitalize = False

#     for char in string:
#         if char.isalpha():
#             if not capitalize:
#                 result.append(char.upper())
#                 capitalize = True
#             else:
#                 result.append(char.lower())
#                 capitalize = False
#         else:
#             result.append(char)
    
#     return "".join(result)