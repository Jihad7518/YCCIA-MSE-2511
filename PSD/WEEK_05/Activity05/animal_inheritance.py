# Part 02 Explanation:
# Yes, different objects can respond differently to the same method call.
# This behavior is known as polymorphism.
# In this project, different animal objects such as Dog, Eagle, and Shark implement the same move() method but behave differently based on their class.
# Polymorphism improves code flexibility, scalability, and allows treating related objects uniformly while preserving specific behavior.


# Part 01 Code Implementation
# animal_inheritance.py
# Demonstrates inheritance based on the provided UML diagram



# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The animal moves.")


# Level 1 Inheritance
class Mammal(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Bird(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


class Fish(Animal):
    def __init__(self, name, feature):
        super().__init__(name)
        self.feature = feature


# Level 2 Inheritance (Concrete Classes)
class Dog(Mammal):
    def walk(self):
        print(f"{self.name} is walking.")

    def move(self):
        print(f"{self.name} walks on four legs.")


class Cat(Mammal):
    def walk(self):
        print(f"{self.name} is walking.")

    def move(self):
        print(f"{self.name} walks gracefully.")


class Eagle(Bird):
    def fly(self):
        print(f"{self.name} is flying.")

    def move(self):
        print(f"{self.name} flies in the sky.")


class Penguin(Bird):
    def swim(self):
        print(f"{self.name} is swimming.")

    def move(self):
        print(f"{self.name} swims instead of flying.")


class Salmon(Fish):
    def swim(self):
        print(f"{self.name} is swimming.")

    def move(self):
        print(f"{self.name} swims upstream.")


class Shark(Fish):
    def swim(self):
        print(f"{self.name} is swimming.")

    def move(self):
        print(f"{self.name} swims powerfully in the ocean.")


# Main Program
if __name__ == "__main__":

    animals = [
        Dog("Buddy", "Has fur"),
        Cat("Kitty", "Has fur"),
        Eagle("Golden Eagle", "Has wings"),
        Penguin("Pingu", "Cannot fly"),
        Salmon("Silver Salmon", "Freshwater fish"),
        Shark("Great White Shark", "Sharp teeth")
    ]

    # Polymorphism Demonstration
    for animal in animals:
        animal.move()