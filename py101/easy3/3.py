# https://launchschool.com/exercises/a2ff3dab

def print_in_box(string):
    length = len(string)
    print(f"+-{'-' * length}-+")
    print(f"| {length * ' '} |")
    print(f"| {string} |")
    print(f"| {length * ' '} |")
    print(f"+-{'-' * length}-+")


print_in_box('To boldly go where no one has gone before.')
print_in_box('')