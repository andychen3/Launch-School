# https://launchschool.com/exercises/53e7afc0

def nums_to_five():
    for num in range(1, 6):
        yield num

for num in nums_to_five():
    print(num)