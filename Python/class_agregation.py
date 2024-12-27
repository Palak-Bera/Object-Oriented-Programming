class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
        
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
        
        
def main():
    a = Address("Ankleshwar", "Gujarat")
    c = Customer("Palak", "Male" , a)
    
    print("Customer's Name : ", c.name)
    print("Customer's Gender : ", c.gender)
    print("Customer's Address : ", c.address.city)
    print("Customer's State : ", c.address.state)
    
if __name__ == "__main__":
    main()