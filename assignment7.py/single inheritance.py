class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Bark"
