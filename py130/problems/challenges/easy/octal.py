# https://launchschool.com/exercises/f39b47fd

"""
input: octal input string
output: decimal output
rules:
1. invalid input as octal 0
2. only valid digits in octal number are 0, 1, 2, 3, 4, 5, 6, 7


DS:


Algo:


"""

class Octal:
    def __init__(self, value):
        self.value = value

    def _validate(self, string):
        for char in string:
            if not char.isdigit() or char not in "01234567":
                return False
        return True

    def to_decimal(self):
        if not self._validate(self.value):
            return 0
        
        total = 0

        for i, num in enumerate(reversed(self.value)):
            total += int(num) * (8 ** i)
        
        return total

