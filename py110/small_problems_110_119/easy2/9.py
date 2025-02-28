# https://launchschool.com/exercises/6051b11c

'''
Questions:


Input:
Output:
Explicit:
Implicit:


Pseudocode:

'''

def count_occurrences(vehicles):
    freq_dict = {}

    for vehicle in vehicles:
        freq_dict.setdefault(vehicle, 0)
        freq_dict[vehicle] += 1

    for vehicle, count in freq_dict.items():
        print(f"{vehicle} => {count}")


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)