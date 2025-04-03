# https://launchschool.com/exercises/ace1735e

"""
input:
output:
rules:


DS:

Algo:


"""
import random
class Robot:
    NAME_SET = set()

    def __init__(self):
        self._name = self.reset()


    @staticmethod
    def _set_name():
        alphabets = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
        digits = list(str(num) for num in range(10))
        name = []

        for i in range(5):
            if i in [0, 1]:
                random_letter = random.choice(alphabets)
                name.append(random_letter)
            else:
                random_digit = random.choice(digits)
                name.append(random_digit)

        # joined_name = "".join(name)

        # Robot.NAME_SET.add(joined_name)

        return "".join(name)

    @property
    def name(self):
        return self._name

    def reset(self):
        """
        Gives new name
        Check if prev name is the same as the new name.
        If so do another random name
        """
        new_name = self._set_name()
        while new_name in Robot.NAME_SET:
            new_name = self._set_name()
        Robot.NAME_SET.add(new_name)
        
        self._name = new_name
        return new_name
    
name1 = Robot().name
print(name1)
print(Robot.NAME_SET)
name2 = Robot().name
print(name2)
print(Robot.NAME_SET)
