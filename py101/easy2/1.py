# https://launchschool.com/exercises/7ad4f1d2?track=python

def greetings(name, status):
    full_name = " ".join(name)
    title = status["title"] + " " + status["occupation"]
    return f"Hello, {full_name}! Nice to have a {title} around."


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.