# https://launchschool.com/exercises/8817379e


def order_by_value(dict1):
    return sorted(dict1, key=dict1.get)


my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True