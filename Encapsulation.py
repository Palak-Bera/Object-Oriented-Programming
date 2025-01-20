class Student:
    def __init__(self, name):
        self.__name = name  # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

# Usage
student = Student("Alice")

# Accessing private attribute through getter
print(student.get_name())  # Output: Alice

# Modifying private attribute through setter
student.set_name("Bob")
print(student.get_name())  # Output: Bob