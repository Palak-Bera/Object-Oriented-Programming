#operator overloading is also called as polymorphism


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overloading the + operator
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        # Overloading the - operator
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        # Overloading the string representation
        return f"({self.x}, {self.y})"


# Example usage:
p1 = Point(2, 3)
p2 = Point(4, 1)

result_add = p1 + p2  # Calls the __add__ method
result_sub = p1 - p2  # Calls the __sub__ method

print(f"Addition: {result_add}")  # Output: Addition: (6, 4)
print(f"Subtraction: {result_sub}")  # Output: Subtraction: (-2, 2)
