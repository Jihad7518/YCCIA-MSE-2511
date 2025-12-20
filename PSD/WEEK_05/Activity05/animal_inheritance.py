# animal_inheritance.py
# Demonstrates inheritance based on the provided UML diagram


# Base class
class Animal:
    def __init__(self, name):
        self.name = name  # Common attribute for all animals


# Mammal inherits from Animal
class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature  # Specific feature of mammals


# Bird inherits from Animal
class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature  # Specific feature of birds


# Fish inherits from Animal
class Fish(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature  # Specific feature of fish


# Dog inherits from Mammal
class Dog(Mammal):
    def walk(self):
        print(f"{self.name} is walking on four legs.")


# Cat inherits from Mammal
class Cat(Mammal):
    def walk(self):
        print(f"{self.name} is walking gracefully.")


# Eagle inherits from Bird
class Eagle(Bird):
    def fly(self):
        print(f"{self.name} is flying high in the sky.")


# Penguin inherits from Bird
class Penguin(Bird):
    def swim(self):
        print(f"{self.name} is swimming in cold water.")


# Salmon inherits from Fish
class Salmon(Fish):
    def swim(self):
        print(f"{self.name} is swimming upstream.")


# Shark inherits from Fish
class Shark(Fish):
    def swim(self):
        print(f"{self.name} is swimming powerfully in the ocean.")


# Main execution
if __name__ == "__main__":

    dog = Dog("Buddy", "Has fur")
    cat = Cat("Whiskers", "Has fur")

    eagle = Eagle("Golden Eagle", "Has wings")
    penguin = Penguin("Emperor Penguin", "Has flippers")

    salmon = Salmon("Atlantic Salmon", "Has gills")
    shark = Shark("Great White Shark", "Has sharp teeth")

    # Calling behavior methods
    dog.walk()
    cat.walk()

    eagle.fly()
    penguin.swim()

    salmon.swim()
    shark.swim()