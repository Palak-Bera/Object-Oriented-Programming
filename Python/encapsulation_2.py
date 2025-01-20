class ATM:
    def __init__(self):
        self.__pin = "" #private Variable
        self._balance = 0 #private Variable
      
        
    #  getter and setter for pin
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        self.__pin = pin
        print("Pin created successfully")
    
class  Bank(ATM):
    def __init__(self):
        super().__init__() #calling parent class constructor      

    def get_protected(self):
        print("Getting Balance (protected Member) using child class getter Method" , self._balance)
        
        
def main():

    x = ATM()
    x.set_pin("656565")
    print("Getting Pin ( private Memeber) using parent class getter Method :", x.get_pin())
    
    y = Bank()
    y.get_protected()
    
if __name__ == "__main__":
    main()
    
#