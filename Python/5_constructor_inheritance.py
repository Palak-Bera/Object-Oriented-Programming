class Phone:
    def __init__(self, brand, model):
        print("inside parent class constructor")
        self.__brand = brand
        self.model = model
        
class Smartphone(Phone):
    pass

def main():
    s = Smartphone("Samsung", "Galaxy S10")
    # print("Smartphone's Brand : ", s.brand)  # accesing private member of parent class
    print("Smartphone's Model : ", s.model)
    
if __name__ == "__main__":
    main()