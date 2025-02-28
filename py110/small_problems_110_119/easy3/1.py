# https://launchschool.com/exercises/86822507?track=python

'''
Questions:


Input: number
Output: string representing the time
Explicit:
1. IF numbers of minutes is positive is after midnight
2. if negative it is before midnight
Implicit:


# Mod the time to keep within 24 hours
# check if number is positive or negative
# if negative subtract from 24 else add the hours
# How to find hours (60 minutes in 1 hour)
# how to find minutes
Pseudocode:


'''

MINUTES_IN_24HOURS = 1440
MINUTES_IN_HOUR = 60


# def time_of_day(time):
#     total_minutes = abs(time) % MINUTES_IN_24HOURS
#     hours = total_minutes / MINUTES_IN_HOUR
#     hour = int(hours)
#     minutes = round((hours - hour) * MINUTES_IN_HOUR)

#     if time < 0: 
#         # time is before midnight subtract the hours from 24
#         after_midnight_hour = 24 - hour - 1
        
#         print(f"{(after_midnight_hour):02d}:{(60 - minutes):02d}")
#     else:
#         # time is after midnight add the hours 
#         print(f"{(hour):02d}:{(minutes):02d}")

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

