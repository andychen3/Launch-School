# https://launchschool.com/exercises/fc450ab6

while True:
    name = input("What is your name? ")

    if name.endswith("!"):
        print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {name}.")