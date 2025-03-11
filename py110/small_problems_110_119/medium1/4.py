# https://launchschool.com/exercises/89604c6e

'''

'''
def check_num(string):
    try:
        int(string)
    except ValueError:
        return False
    return True


def minilang(commands):
    stack = []
    register = 0
    split_command = commands.split()

    for command in split_command:
        if check_num(command):
            register = int(command)
        elif command == "PRINT":
            print(register)
        elif command == "PUSH":
            stack.append(register)
        elif command == "ADD":
            register = register + stack.pop()
        elif command == "SUB":
            register = register - stack.pop() 
        elif command == "MULT":
            register = register * stack.pop()
        elif command == "DIV":
            register = register // stack.pop()
        elif command == "REMAINDER":
            register = register % stack.pop()
        elif command == "POP":
            register = stack.pop()
        
minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)
        

