# https://launchschool.com/exercises/ae91b171

# while True:
#     first_num = float(input("==> Enter the first number:\n "))
#     second_num = float(input("==> Enter the second number:\n "))

#     print(f"{first_num} + {second_num} = {first_num + second_num}")
#     print(f"{first_num} - {second_num} = {first_num - second_num}")
#     print(f"{first_num} * {second_num} = {first_num * second_num}")
#     print(f"{first_num} / {second_num} = {first_num / second_num}")
#     print(f"{first_num} // {second_num} = {first_num // second_num}")
#     print(f"{first_num} % {second_num} = {first_num % second_num}")
#     print(f"{first_num} ** {second_num} = {first_num ** second_num}")


def calculate(operator, operand1, operand2):
    match operator:
        case "+":
            return operand1 + operand2
        case "-":
            return operand1 - operand2
        case "*":
            return operand1 * operand2
        case "/":
            return operand1 / operand2
        case "//":
            return operand1 // operand2
        case "**":
            return operand1 ** operand2
        case "%":
            return operand1 % operand2

prompt1 = float(input("==> Enter the first number:\n "))
prompt2 = float(input("==> Enter the second number:\n "))

for operator in ["+", "-", "*", "/", "//", "%", "**"]:
    result = calculate(operator, prompt1, prompt2)
    print(f"==> {prompt1} {operator} {prompt2} = {result}")