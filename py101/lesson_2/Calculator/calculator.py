# Ask the user for two numbers
# ask the user for the type of operation to perform
# List of operations are add, subtract, multiply, and divide
# Perform the calculation and display the result

# Ask the user for the first number
# ask the user for the second number
# Ask the user which operation to perform
# Perform operation on the two numbers with operation that was selected
# display the results

# operation_dict = {"+": first_number + second_number,
#                   "-": first_number - second_number,
#                   "*": first_number * second_number,
#                   "/": first_number / second_number}


def prompt(message):
    print(f"=> {message}")


def is_valid_number(number):
    try:
        int(number)
    except ValueError:
        return False
    return int(number)


prompt("Welcome to Calculator!")

prompt("Enter the first number: ")
first_number = is_valid_number(input())

while not first_number:
    prompt("Please enter a valid number.")
    first_number = is_valid_number(input())


prompt("Enter the second number: ")
second_number = is_valid_number(input())

while not second_number:
    prompt("Please enter a valid number.")
    second_number = is_valid_number(input())


prompt("You can select these four operations: (+, -, *, /)")
prompt("Select the operation to perform: ")
operation = input()

while operation not in ["+", "-", "/", "*"]:
    prompt("Please enter a valid operation.")
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
