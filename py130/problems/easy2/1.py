# https://launchschool.com/exercise_sets/73545447?track=python

def greet(name, greeting, punc="."):
    return f"{greeting}, {name}{punc}"

print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good Morning, Pete!

