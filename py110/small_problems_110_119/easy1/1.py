# https://launchschool.com/exercises/a1c4fed5?track=python

def searching_101():
    suffix_dict = {1: "1st", 2: "2nd", 3: "3rd", 4: "4th", 5: "5th", 6: "last"}
    answer_list = []
    number_of_inputs = 1
    last_number = None

    while number_of_inputs != 7:
        number = input(f"Enter the {suffix_dict[number_of_inputs]} number: ")

        if number_of_inputs == 6:
            last_number = number
            break

        number_of_inputs += 1
        answer_list.append(number)
    
    if last_number in answer_list:
        print(f"{last_number} is in {','.join(answer_list)}.")
    else:
        print(f"{last_number} isn't in {','.join(answer_list)}.")


searching_101()