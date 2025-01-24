# https://launchschool.com/exercises/bf23e529

from datetime import datetime as date

while True:
    age = int(input("What is your age? "))
    retire_age = int(input("At what age would you like to retire? "))

    current_year = int(date.today().year)
    distance_to_retirement = retire_age - age
    retirement_year = current_year + distance_to_retirement
    print(f"It's {current_year}. You will retire in {retirement_year}.")
    print(f"You have only {distance_to_retirement} years of work to go!")


