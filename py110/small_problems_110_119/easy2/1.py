# https://launchschool.com/exercises/3292ee85?track=python

'''
Questions:


Input: floating point number to represent a degree
Output: strings that represents degree, minute, and seconds
Explicit:
1. Floating point number
2. 60 minutes in a degree
3. 60 seconds in a minute.
4. only degrees from 0-360
Implicit:
1. 


Pseudocode:
1. Three methods. 
'''

DEGREE = "\u00B0"

def pad_zero(number):
    string_number = str(number)
    if len(string_number) < 2:
        return "0" + string_number
    return number

def dms(degree_float):
    degree_int = int(degree_float)
    minutes_float = (degree_float - degree_int) * 60
    seconds_int = int(minutes_float)
    seconds = (minutes_float - seconds_int) * 60


    return f"{degree_int}{DEGREE}{pad_zero(int(minutes_float))}'{pad_zero(int(seconds))}\""

# All of these examples should print True
print(dms(30) == "30°00'00\"")
print(dms(76.73) == "76°43'48\"")
print(dms(254.6) == "254°35'59\"")
print(dms(93.034773) == "93°02'05\"")
print(dms(0) == "0°00'00\"")
print(dms(360) == "360°00'00\"" or dms(360) == "0°00'00\"")



