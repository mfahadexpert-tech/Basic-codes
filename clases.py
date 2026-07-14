class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print(f"{self.name} makes a sound.")
class bird(animal):
    def __init__(self, name, species, can_fly):
        super().__init__(name, species)
        self.can_fly = can_fly

    def make_sound(self):
        print(f"{self.name} chirps.")
s=bird("Parrot", "Bird", True)        
print(s.make_sound())