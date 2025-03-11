# https://launchschool.com/exercises/2fb67370

"""


"""
import datetime

def friday_the_13ths(year):

    thirteen = [datetime.date(year, month, 13) for month in range(1, 13)]
    
    num_of_fridays = 0

    for days in thirteen:
        if datetime.datetime.isoweekday(days) == 5:
            num_of_fridays += 1
    
    return num_of_fridays
    



print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True