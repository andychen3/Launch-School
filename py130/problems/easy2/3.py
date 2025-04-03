# https://launchschool.com/exercises/66b8ad5e

def build_profile(first, last, **kwargs):
    return {'first_name': first, 'last_name': last} | kwargs
    

print(build_profile("Max", "Hawkins", location="San Francisco", field="Software Engineering"))
# {'first_name': 'Max', 'last_name': 'Hawkins', 'location': 'San Francisco', 'field': 'Software Engineering'}