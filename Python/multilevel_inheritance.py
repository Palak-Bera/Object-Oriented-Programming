# Base class
class Grandparent:
    def greet(self):
        print("Hello from Grandparent!")

# Intermediate class
class Parent(Grandparent):
    def greet_parent(self):
        print("Hello from Parent!")

# Derived class
class Child(Parent):
    def greet_child(self):
        print("Hello from Child!")

# Usage
child = Child()
child.greet()         # From Grandparent
child.greet_parent()  # From Parent
child.greet_child()   # From Child
