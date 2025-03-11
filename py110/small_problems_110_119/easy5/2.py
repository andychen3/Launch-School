# https://launchschool.com/exercises/4b19afa8

def keep_keys(input_dict, keys):
    return {key: input_dict[key] for key in keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True