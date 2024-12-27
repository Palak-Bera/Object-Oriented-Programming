class Customer:
    def __init__(self, name):
        self.name = name
      

def new_method(cust):
    print("Passing object into new_method :" , id(cust.name))
    cust.name = "Bera"
    print("Changing object's variable :", id(cust.name))
    print("Object's variable after change :", cust.name)
    
def main():
    c = Customer("Palak")
    print("Original ID during Class :", id(c.name))
    new_method(c[:])
    print( "Object's variable after change in main : ", c.name)
    
if __name__ == "__main__":
    main()