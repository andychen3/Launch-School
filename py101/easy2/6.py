# https://launchschool.com/exercises/1f88d422

# def penultimate(str):
#     return str.split()[-2]

# # These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")


# Further Exploration
# no words or one word

def penultimate(str):
     word_split = str.split()
     
     if len(word_split) <= 2:
          return str
     
     middle = len(word_split) // 2
     # even length can return both middle ones
     if middle % 2 == 0:
        return f"{word_split[middle - 1]} {word_split[middle]}"
     else:
     # odd length
        return word_split[middle]
     

print(penultimate("last") == "last")
print(penultimate("") == "")
print(penultimate("last word") == "last word")
print(penultimate("Launch School is great!") == "School is")
print(penultimate("Launch School great!") == "School")

# odd and even length middle. 