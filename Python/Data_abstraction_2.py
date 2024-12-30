from abc import ABC, abstractmethod

class Drawable(ABC):  # Interface
    @abstractmethod
    def draw(self):
        pass  # Abstract method, must be implemented

class Circle(Drawable):  # Implements the interface
    def draw(self):
        return "Drawing a circle"

class Square(Drawable):  # Implements the interface
    def draw(self):
        return "Drawing a square"

# Usage
shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.draw())
