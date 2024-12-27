# Parent class
class Parent:
    def greet(self):
        print("Hello from Parent!")

# Child class
class Child(Parent):
    def greet_child(self):
        print("Hello from Child!")

# Usage
child = Child()
child.greet()  # Accessing parent method
child.greet_child()
