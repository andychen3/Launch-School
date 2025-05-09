# https://launchschool.com/exercises/c9dff226

class Vehicle:

    def __init__(self, make, model, wheels):
        self.make = make
        self.model = model
        self.wheels = wheels
    
    def get_wheels(self):
        return self.wheels

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 4)


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 2)

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model, 6)
        self.payload = payload
