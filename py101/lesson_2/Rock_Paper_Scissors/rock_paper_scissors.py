'''
Rock Paper Scissors Spock Lizard Application
'''
import json
import random
import os

VALID_CHOICES = ["rock", "scissor", "paper", "spock", "lizard"]
player_dict = {"You": 0, "Computer": 0}

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
            case "s":
                return False
            case selection if selection and any(choice.startswith(selection)
                                                for choice in VALID_CHOICES):
                return True
            case _:
                return False
    except ValueError:
        return False


def validate_shorthand_user_choice(user_choice):
    '''
    Further validation for user_choice that is shorthand
    '''
    if user_choice in VALID_CHOICES:
        return user_choice

    for choice in VALID_CHOICES:
        if choice.startswith(user_choice):
            return choice

    return None


def select_user_choice():
    '''
    User selects choice
    '''
    prompt(MESSAGES["game_choices"])
    choice = input()

    while not validate_user_choice(choice):
        print(MESSAGES["invalid_choice"])
        choice = input()

    return choice.lower()


def select_computer_choice():
    '''
    Computer selects choice
    '''
    return random.choice(VALID_CHOICES)


def display_winner(user_selection, computer_selection):
    '''
    Determines who is the winner.
    '''
    user_selection = validate_shorthand_user_choice(user_selection)

    prompt(f"You chose {user_selection} | "
           f"computer chose {computer_selection}.")

    if user_selection == computer_selection:
        return "Tie"

    winning_cases = {
        "rock": ["scissor", "lizard"],
        "paper": ["rock", "spock"],
        "scissor": ["paper", "lizard"],
        "spock": ["scissor", "rock"],
        "lizard": ["paper", "spock"],
    }

    if computer_selection in winning_cases[user_selection]:
        return "You"
    return "Computer"


def decide_winner(winning_player):
    '''
    Tallys up the winner.
    Winner is declared if their wins equals 3.
    '''
    if winning_player == "Tie":
        return False

    player_dict[winning_player] += 1

    prompt(f"Your score is {player_dict['You']} | "
           f"computer score is {player_dict['Computer']}")

    if player_dict[winning_player] == 3:
        prompt(f"The winner is {winning_player}!")
        return True
    return False


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


def play_game():
    '''
    Starts the game.
    '''
    prompt(MESSAGES["welcome"])
    match_over = False

    while True:
        user_choice = select_user_choice()
        computer_choice = select_computer_choice()

        winner = display_winner(user_choice, computer_choice)

        match_over = decide_winner(winner)

        if match_over:
            prompt(MESSAGES["play_again"])
            command = input()

            command = validate_continuation_command(command)

            if command == "no":
                break
            if command == "yes":
                os.system("clear")
                player_dict["You"] = 0
                player_dict["Computer"] = 0
                continue


play_game()
