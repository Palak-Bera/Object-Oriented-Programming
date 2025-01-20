class MyClass:
    # Static variable
    count = 0
    
    def __init__(self, name):
        self.name = name
        MyClass.count += 1  # Increment count for each new instance
    
    # Static method
    @staticmethod
    def greet():
        print("Hello! This is a static method.")

    # Instance method to show static variable
    def show_count(self):
        print(f"Total instances: {MyClass.count}")

# Usage
obj1 = MyClass("Alice")
obj2 = MyClass("Bob")

# Access static method
MyClass.greet()  # Output: Hello! This is a static method.

# Access static variable through instance
obj1.show_count()  # Output: Total instances: 2

# Access static variable through class
print(MyClass.count)  # Output: 2