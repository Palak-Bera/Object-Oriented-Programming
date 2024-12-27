# Parent classes
class Parent1:
    def greet1(self):
        print("Hello from Parent1!")

class Parent2:
    def greet2(self):
        print("Hello from Parent2!")

# Child class
class Child(Parent1, Parent2):
    pass

# Usage
child = Child()
child.greet1()
child.greet2()
