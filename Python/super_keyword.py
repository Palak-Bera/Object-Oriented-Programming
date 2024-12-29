# # Super() keyword always works inside the class and it is used to call the parent class methods and constructor

# class Phone:
#     def __init__(self, brand, model, price):
#         print("Inside Parent class constructor")
#         self.brand = brand
#         self.model = model
#         self.price = price

# class Smartphone(Phone):
#     def __init__(self, brand, model, price, ram, internal_memory, rear_camera):
#         super().__init__(brand, model, price)
#         print("Inside Child class constructor")
#         self.ram = ram
#         self.internal_memory = internal_memory
#         self.rear_camera = rear_camera
        

        
# def main():
#     s = Smartphone("Samsung", "Galaxy S20", 70000, "8GB", "128GB", "64MP")
#     print(s.brand)
#     print(s.ram)

# if __name__ == "__main__":
#     main()
    
    
class Parent:
    def __init__(self):
        self.num = 100
    
    def parent_method(self):
        print("Inside Parent class method accessing through child self")
    
    def parent_method2(self):
        print("Inside Parent class method accessing through super")
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.var = 200
        
    def show(self):
        print(self.num)
        print(self.var)
        print(self.parent_method())
        print(super().parent_method2())
        
def main():
    x = Child()
    x.show()
    
if __name__ == "__main__":
    main()


# method resolution order is used in multiple inheritance     
      