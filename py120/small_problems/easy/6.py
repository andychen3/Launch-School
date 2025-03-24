# https://launchschool.com/exercises/8c2d2017

class Pet:

    def __init__(self, species, name):
        self._species = species
        self._name = name
    
    @property
    def species(self):
        return self._species
    
    @property
    def name(self):
        return self._name
    
class Owner:

    def __init__(self, name):
        self._name = name
        self.pets = 0

    @property
    def name(self):
        return self._name
    
    def number_of_pets(self):
        return self.pets

    def add_pet(self):
        self.pets += 1

class Shelter:

    def __init__(self):
        self.registry = {}

    def adopt(self, owner, pet):
        if owner not in self.registry:
            self.registry[owner] = []
        self.registry[owner].append(pet)
        owner.add_pet()

    def print_adoptions(self):
        for owner, list_of_pets in self.registry.items():
            print(f"{owner.name} has adopted the following pets:")
            for pet in list_of_pets:
                print(f"a {pet.species} named {pet.name}")
            print()

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
