# Problems 
# Variables as Pointers end of chapter problems

# 1
#In your own words, explain the difference between these two expressions.
# my_object1 == my_object2
# The difference is this is looking at if the two variables have equal elements

# my_object1 is my_object2
# This is checking if they are pointing to the same object. Which means
# if they object they are pointing to is the same one located in memory.


# 2
# Without running this code, what will it print? Why?
# set1 = {42, 'Monty Python', ('a', 'b', 'c')}
# set2 = set1
# set1.add(range(5, 10))
# print(set2)

# It will print {42, 'Monty Python', ('a', 'b', 'c'), range(5,10)}
# Reasoning is set2 is set to equal set1. So it's alias is set1. Thus
# when something is mutated in set1 it will show up in set2 since set2 is
# referencing the same object as set1. This
# shows that assigning a variable to another variable doesn't create a new ojbect.
# It copies a reference from the original variable to the new variable.


# 3
# Without running this code, what will it print? Why?
# dict1 = {
#     "Hitchhiker's Guide to the Galaxy": 42,
#     'Monty Python': 'The Life of Brian',
#     'Airplane!': "Don't call me Shirley!",
# }

# dict2 = dict(dict1)
# dict2['Monty Python'] = 'Holy Grail'
# print(dict1['Monty Python'])

# This will print # dict1 = {
#     "Hitchhiker's Guide to the Galaxy": 42,
#     'Monty Python': 'The Life of Brian',
#     'Airplane!': "Don't call me Shirley!",
# }
# Reasoning is that dict2 created a shallow copy of dict1. This means 
# dict2 has it's own copy of dict1 and is its own object. Thus when you modify dict1
# it does not show up in dict2 and vice versa.


# 4
# Without running this code, what will it print? Why?
# dict1 = {
#     'a': [1, 2, 3],
#     'b': (4, 5, 6),
# }

# dict2 = dict(dict1)
# dict1['a'][1] = 42
# print(dict2['a'])


#     'a': [1, 42, 3]

# The reasoning is because dict2 only created a shallow copy of dict1.
# everything on the outer collection is copied but the inner collections are not.
# the inner collections all hold a reference to where the collections are stored.
# so when an inner collection is modified it shows the modification in dict1 or dict2




# 5 
# Write some code to create a deep copy of the dict1 object and 
# assign it to dict2. You should only modify the code where indicated.


# You may modify this line
# import copy

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = copy.deepcopy(dict1)

# # All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])
# # All of these should print True

# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])

# 6
# The following program is nearly identical 
# to that of the previous exercise. However, this time, it should
#  create a shallow copy of dict1. Be careful: you're not allowed to
#  use the copy module in this exercise.`

# In addition, before you run this code, can you predict the output values?

dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2) # False
print(dict1['a']    is dict2['a']) # True
print(dict1['a'][0] is dict2['a'][0]) # True
print(dict1['a'][1] is dict2['a'][1]) # True
print(dict1['b']    is dict2['b']) # True
print(dict1['b'][0] is dict2['b'][0]) # True
print(dict1['b'][1] is dict2['b'][1]) # True
