# https://launchschool.com/exercises/634f48e3

def signed_integer_to_string(number):
    string_number = ""
    input_number = abs(number)
    sign = "+" if number > 0 else "-"

    while input_number:
        digit = input_number % 10
        string_number += chr(digit + 48)
        input_number //= 10

    return sign + string_number[::-1] if string_number else "0"

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True


# Better performance but not concise
# def signed_integer_to_string(number):
#     string_number = []
#     input_number = number
#     sign = None
    
#     if number < 0:
#         input_number *= -1
#         sign = "-"
#     elif number > 0:
#         sign = "+"


#     while input_number:
#         digit = input_number % 10
#         string_number.append(chr(digit + 48))
#         input_number = input_number // 10

#     if sign:
#         string_number.append(sign)

#     return "".join(string_number[::-1]) or "0"