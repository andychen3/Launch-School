# Ask the user for two numbers
# ask the user for the type of operation to perform
# List of operations are add, subtract, multiply, and divide
# Perform the calculation and display the result

# Ask the user for the first number
# ask the user for the second number
# Ask the user which operation to perform
# Perform operation on the two numbers with operation that was selected
# display the results
import json

with open("calculator_messages.json", "r") as file:
    data = json.load(file)


def prompt(message):
    print(f"=> {message}")


def is_valid_number(number):
    try:
        float(number)
    except ValueError:
        return False
    return float(number)


while True:
    prompt(data["messages"]["welcome"])

    prompt(data["messages"]["input_first_number"])
    first_number = is_valid_number(input())

    while not first_number:
        prompt(data["messages"]["Invalid_number"])
        first_number = is_valid_number(input())

    prompt(data["messages"]["input_second_number"])
    second_number = is_valid_number(input())

    while not second_number:
        prompt(data["messages"]["Invalid_number"])
        second_number = is_valid_number(input())

    prompt(data["messages"]["operation_choices"])
    prompt(data["messages"]["select_operation"])
    operation = input()

    while operation not in ["+", "-", "/", "*"]:
        prompt(data["messages"]["Invalid_operation"])
        operation = input()

    match operation:
        case "+":
            result = first_number + second_number
        case "-":
            result = first_number - second_number
        case "*":
            result = first_number * second_number
        case "/":
            result = first_number / second_number

    prompt(f"{first_number} {operation} {second_number} = {result}")
    prompt(data["messages"]["another_operation"])
    answer = input()
    if answer and answer[0].lower() != "y":
        break
