# https://launchschool.com/exercises/44718e8c

'''
Questions:


Input:
Output:
Explicit:
Implicit:


Pseudocode:

'''

MINUTES_IN_HOUR = 60


def after_midnight(time):
    # You add the minutes
    split_time = time.split(":")
    if split_time[0] == "24":
        return 0

    hours = int(split_time[0])
    minutes = int(split_time[1])

    return hours * MINUTES_IN_HOUR + minutes


def before_midnight(time):
    # You subtract the minutes
    split_time = time.split(":")
    if split_time[0] == "24":
        return 0
    hours = int(split_time[0])
    minutes = int(split_time[1])

    return hours * MINUTES_IN_HOUR - minutes

print(before_midnight("22:00") == 1320)    # True
# print(after_midnight("00:00") == 0)     # True
# print(before_midnight("00:00") == 0)    # True
# print(after_midnight("12:34") == 754)   # True
# print(before_midnight("12:34") == 686)  # True
# print(after_midnight("24:00") == 0)     # True
# print(before_midnight("24:00") == 0)    # True