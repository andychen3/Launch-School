# https://launchschool.com/exercises/58127fca

import random

# def generate_age():
#     age = random.randint(20, 100)
#     print(f"Teddy is {age} years old!")

# generate_age()


# Further exploration
import random

while True:
    name = input("Enter a name please: ")
    age = random.randint(20, 100)
    if name:
        print(f"{name} is {age} years old!")
    else:
        print(f"Teddy is {age} years old!")