# https://launchschool.com/exercises/ada66137


def get_input():
    while True:
        user_input = input("Give strings until the stop command: ")
        yield user_input

        if user_input == "stop":
            break

for word in get_input():
    print(word)