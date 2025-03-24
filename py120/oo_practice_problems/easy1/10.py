# https://launchschool.com/lessons/a6479eb0/assignments/bf55fc72


class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

"""
The _cats_count variable is a class variable of the Cat class. It represents
the number of Cat objects that get initiated. You can see this when in the
initializer it increments the varaible everytime a new cat class is created. 


"""