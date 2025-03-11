# https://launchschool.com/exercises/267890f0?track=python

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')



# counter = 10

# for _ in range(10):
#     print(counter)
#     counter -= 1

# print('LAUNCH!')