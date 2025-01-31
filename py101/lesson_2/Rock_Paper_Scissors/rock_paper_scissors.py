'''
Rock Paper Scissors Spock Lizard Application
'''
import json
import random

VALID_CHOICES = ["rock", "scissor", "paper", "spock", "lizard"]

with open("rps_messages.json", "r", encoding="utf-8") as file:
    MESSAGES = json.load(file)


def prompt(messages):
    '''
    Makes message output easier to read.
    '''
    print(f"==> {messages}")


def validate_user_choice(selection):
    '''
    Validates user's input
    '''
    try:
        selection = selection.lower()

        match selection:
            case selection if selection in VALID_CHOICES:
                return True
            case _:
                return False
    except ValueError:
        return False


def select_user_choice():
    '''
    User selects choice
    '''
    prompt(MESSAGES["game_choices"])
    choice = input()

    while not validate_user_choice(choice):
        print(MESSAGES["invalid_choice"])
        choice = input()

    return choice


def select_computer_choice():
    '''
    Computer selects choice
    '''
    random_choice = random.randint(0, 4)

    match random_choice:
        case 0:
            return "rock"
        case 1:
            return "paper"
        case 2:
            return "scissor"
        case 3:
            return "spock"
        case 4:
            return "lizard"


def display_winner(user_selection, computer_selection):
    '''
    Determines who is the winner.
    '''
    prompt(f"You chose {user_selection}, computer chose {computer_selection}.")

    if user_selection == computer_selection:
        prompt("The match ended in a Tie.")

    winning_cases = {
        "rock": ["scissor", "lizard"],
        "paper": ["rock", "spock"],
        "scissor": ["paper", "lizard"],
        "spock": ["scissor", "rock"],
        "lizard": ["paper", "spock"],
    }

    if computer_selection in winning_cases[user_selection]:
        prompt("The winner is you!")
    else:
        prompt("The winner is the computer!")


def play_game():
    '''
    Starts the game.
    '''
    prompt(MESSAGES["welcome"])

    while True:
        user_choice = select_user_choice()
        computer_choice = select_computer_choice()

        display_winner(user_choice, computer_choice)

        prompt(MESSAGES["play_again"])
        answer = input()

        if answer and answer.lower()[0] != "y":
            break


play_game()
