# ABC is the base class for creating abstract classes.
# abstractmethod is used to enforce the implementation of specific methods in subclasses.
# from abc import ABC, abstractmethod
# Use ABC and abstractmethod when you need to enforce a specific contract (i.e., mandatory methods) across multiple subclasses. 
# For example, all shapes should have area() and perimeter() methods, regardless of their type (circle, rectangle, etc.).
# An abstract class serves as a blueprint for other classes.
# you cannot create an instance of an abstract class.

#

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):
        pass  # Abstract method

    @abstractmethod
    def perimeter(self):
        pass  # Abstract method

    # Concrete method
    def description(self):
        return "This is a shape"

class Rectangle(Shape):  # Concrete class
    def __init__(self, width, height):
        print("Calling Abstract class method using super()")
        print(super().description())
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    # Overriding the concrete method
    def description(self):
        return f"This is a rectangle with width {self.width} and height {self.height}"

# Usage
rect = Rectangle(10, 20)
# shape = Shape()  
print(rect.description())          # Output: This is a rectangle with width 10 and height 20
print(f"Area: {rect.area()}")      # Output: Area: 200
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 60
