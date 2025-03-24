# https://launchschool.com/exercises/db67bc69

import random
import math

class GuessingGame:

    def __init__(self, low, high):
        self.guesses = int(math.log2(high - low + 1)) + 1
        self.correct_number = None
        self.low = low
        self.high = high

    def _validate_number(self, num):
        if num < self.low or num > self.high:
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
        self.correct_number = random.randint(self.low, self.high)

        while self.guesses != 0:
            print(f"You have {self.guesses} guesses remaining.")
            while True:
                number = int(input(f"Enter a number between {self.low} and {self.high}: "))

                if not self._validate_number(number):
                    break
                
                print("Invalid guess.")

            if self.check_if_correct_number(number):
                break

            self.guesses -= 1
        
        if self.guesses == 0:
            print("You have no more guesses. You lost!")
        

game = GuessingGame(200, 1500)
game.play()
