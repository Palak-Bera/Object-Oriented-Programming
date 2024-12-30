# Method overriding ( Dynamic polymorphism)



# Parent class
class Animal:
    def speak(self):
        return "The animal makes a sound"

# Subclass
class Dog(Animal):
    def speak(self):
        return "The dog barks"

class Cat(Animal):
    def speak(self):
        return "The cat meows"

# Create instances
animal = Animal()
dog = Dog()
cat = Cat()

# Call the speak method
print(animal.speak())  # Output: The animal makes a sound
print(dog.speak())     # Output: The dog barks
print(cat.speak())     # Output: The cat meows
