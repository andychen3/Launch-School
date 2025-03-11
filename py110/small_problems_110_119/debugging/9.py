# https://launchschool.com/exercises/3c9bd095

data_set = {1, 2, 3, 4, 5}
new_data_set = set()

for item in data_set:
    if item % 2 == 0:
        new_data_set.add(item)

data_set = new_data_set