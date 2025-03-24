# https://launchschool.com/exercises/7b0e1c18

class FlyingMixin:
    def fly(self):
        return "I'm flying!"

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(FlyingMixin, Animal):
    pass

bird1 = Bird('Red')
print(bird1.color)

# bird: bird -> FlyingMixin -> Animal