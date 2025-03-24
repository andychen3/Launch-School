# https://launchschool.com/exercises/7f1293f5

class Cat:
    CAT_COLOR = "purple"

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello, my name is {self.name} and I'm a {Cat.CAT_COLOR} cat!")
    
kitty = Cat("Sophie")
kitty.greet()