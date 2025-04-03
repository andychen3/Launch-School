# https://launchschool.com/exercises/7aa71d61

def display_info(data, /, *, reverse=False, uppercase=False):
    new_data = data
    if reverse:
        new_data = new_data[::-1]
    
    if uppercase:
        new_data = new_data.upper()
    
    return new_data

print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC