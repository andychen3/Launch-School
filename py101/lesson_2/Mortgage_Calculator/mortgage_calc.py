'''
Mortgage Calculator App
'''

import json
import os

with open("mortgage_messages.json", "r", encoding="utf-8") as file:
    MESSAGES = json.load(file)


def prompt(message):
    '''
    Modifies messages output.
    '''
    print(f"=> {message}")


def is_valid_number(number):
    '''
    Tests if number is greater than 0 and not infinity.
    '''
    try:
        num = float(number)
        if num >= 0 and num != float("inf") \
                and num != float("-inf"):
            return True
        return False
    except ValueError:
        return False


def convert_apr(interest_rate):
    '''
    Converts annual interest rate into a decimal and monthly.
    '''
    return (interest_rate / 100) / 12


def check_loan_duration(year):
    '''
    Tests that year is a whole number and greater than 0.
    '''
    try:
        if int(year) and int(year) > 0 and len(year.split(".")) == 1:
            return True
        return False
    except ValueError:
        return False


def calc_mortgage_payment(loan, interest_rate, loan_duration):
    '''
    Monthly mortgage payment calculation
    '''
    if interest_rate == 0:
        return loan / loan_duration

    return loan * (interest_rate / (1 - (1 + interest_rate)
                                    ** (-loan_duration)))


def validate_user_input(message):
    '''
    Validates and returns user input
    '''
    while True:
        prompt(MESSAGES[message])
        user_input = input()

        if is_valid_number(user_input):
            return float(user_input)

        prompt(MESSAGES["invalid_number"])


def get_loan_duration():
    '''
    Returns loan duration entered by user
    '''
    while True:
        prompt(MESSAGES["input_loan_duration"])
        loan_duration_in_years = input()

        if check_loan_duration(loan_duration_in_years):
            return int(loan_duration_in_years)

        prompt(MESSAGES["invalid_loan_duration"])


def loan_calculator():
    '''
    Main function of loan calculator
    '''
    loan_amount = validate_user_input("input_loan_amount")
    apr = convert_apr(validate_user_input("input_apr"))
    loan_duration_in_years = get_loan_duration()

    loan_duration_in_months = loan_duration_in_years * 12

    monthly_payment = calc_mortgage_payment(loan_amount,
                                            apr, loan_duration_in_months)

    prompt(f"Your monthly mortgage payment is ${monthly_payment:.2f}.")


def validate_continuation_command(command):
    '''
    Validates if user wants to continue the game.
    '''
    while not command or command != "no" or command != "yes":
        if command in ["yes", "no"]:
            return command
        prompt(MESSAGES["invalid_command"])
        command = input().lower()
    return command


def run_application():
    '''
    Starts program.
    '''
    prompt(MESSAGES["welcome"])

    while True:
        loan_calculator()

        prompt(MESSAGES["another_calculation"])
        response = input().lower()

        command = validate_continuation_command(response)

        if command == "no":
            break
        if command == "yes":
            os.system("clear")
            continue


run_application()
