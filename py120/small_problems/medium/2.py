# https://launchschool.com/exercises/f4e85bbd

import random

class GuessingGame:

    def __init__(self):
        self.guesses = None
        self.correct_number = None

    def _validate_number(self, num):
        if num < 1 or num > 100:
            return True
        return False

    def check_if_correct_number(self, num):
        if num > self.correct_number:
            print("Your guess is too high.")
            return False
        elif num < self.correct_number:
            print("Your guess is too low.")
            return False
        else:
            print("That's the number!")
            print("You won!")
            return True

    def play(self):
        """
        Calls a method that tells user how many guesses tehy have
        Ask user for a number between 1 and 100
        Check validation
        """
        self.guesses = 7
        self.correct_number = random.randint(1, 100)

        while self.guesses != 0:
            print(f"You have {self.guesses} guesses remaining.")
            while True:
                number = int(input("Enter a number between 1 and 100: "))

                if not self._validate_number(number):
                    break
                
                print("Invalid guess.")
            # If number is the guess break
            if self.check_if_correct_number(number):
                break

            self.guesses -= 1
        
        if self.guesses == 0:
            print("You have no more guesses. You lost!")
        

game = GuessingGame()
game.play()
