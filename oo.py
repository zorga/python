# Exercises on Object oriented programming in Python

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class MyClass:
    """A simple example class"""
    i = 12345
    def hello(self):
        return "Hello World!"

class Dog:
    kind = "canine" # class variable shared by all instances of Dog

    def __init__(self, name):
        self.name = name #instance variable
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

if __name__ == '__main__':
    pass
