# https://launchschool.com/exercises/9e90e4a5


def is_balanced(string):
    stack = []

    for char in string:
        if not stack and char == ")":
            return False
        elif char == "(":
            stack.append(char)
        elif char == ")" and stack[-1] == "(":
            stack.pop()
    
    return not stack

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True