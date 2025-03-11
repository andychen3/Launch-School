"""

input: integer
output: string. But signed
rules:
1. negative numberhave to have -
2. positive have to have +

[1]

4321 % 10 = 1
append(chr(1 + 48))
4321 // 10 = 432

Algo:
1. have number = input
2. res = []
3. positive = True if input > 0 else False
4. Create while loop and set it to number
5. get the remainder by modding the number by 10
6. appending this number to result after converting it to a string
7. integer division the number
8. if positive is true append + else append -
9. return the number if res is not empty

"""

def signed_integer_to_string(num):
    if num == 0:
        return "0"
    positive = True if num >= 0 else False
    number = abs(num)
    res = []

    while number:
        remainder = number % 10
        res.append(chr(remainder + 48))
        number //= 10

    if positive:
        res.append("+")
    else:
        res.append("-")

    return "".join(res[::-1])

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True
