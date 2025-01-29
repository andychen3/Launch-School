'''
Mortgage Calculator App
'''

import json

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
        if num > 0 and num != float("inf") \
                and num != float("-inf"):
            return True
        return False
    except ValueError:
        return False


def convert_apr(interest_rate):
    '''
    Converts annual interest rate into a decimal and monthly.
    '''
    return (float(interest_rate) / 100) / 12


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
    return loan * (interest_rate / (1 - (1 + interest_rate)
                                    ** (-loan_duration)))


def loan_calculator():
    '''
    Main function of loan calculator
    '''
    while True:
        # Ask for loan amount
        prompt(MESSAGES["input_loan_amount"])
        loan_amount = input()

        if is_valid_number(loan_amount):
            loan_amount = float(loan_amount)
            break

        prompt(MESSAGES["invalid_number"])

    while True:
        # Ask for APR
        prompt(MESSAGES['input_apr'])
        apr = input()

        if is_valid_number(apr):
            apr = convert_apr(apr)
            break

        prompt(MESSAGES["invalid_number"])

    while True:
        # Ask for loan duration
        prompt(MESSAGES["input_loan_duration"])
        loan_duration_in_years = input()

        if check_loan_duration(loan_duration_in_years):
            loan_duration_in_years = int(loan_duration_in_years)
            break

        prompt(MESSAGES["invalid_loan_duration"])

    loan_duration_in_months = loan_duration_in_years * 12

    monthly_payment = calc_mortgage_payment(loan_amount,
                                            apr, loan_duration_in_months)

    prompt(f"Your monthly mortgage payment is ${monthly_payment:.2f}.")


def run_application():
    '''
    Starts program.
    '''
    while True:
        prompt(MESSAGES["welcome"])
        loan_calculator()

        prompt(MESSAGES["another_calculation"])
        response = input()
        if response and response[0].lower() != "y":
            break


run_application()
