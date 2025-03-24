# https://launchschool.com/exercises/4f5e51c1

class WalkingMixin:

    def walk(self):
        return f"{self.name} {self.gait()} forward"
    
class Person(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"
    
    

class Cat(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"


class Cheetah(WalkingMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
