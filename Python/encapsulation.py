class ATM:
    def __init__(self):
        self.__pin = "" #private Variable
        self.__balance = 0 #private Variable
      
        
    #  getter and setter for pin
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, pin):
        self.__pin = pin
        print("Pin created successfully")
        

def main():

    x = ATM()
    x.set_pin("656565")
    print("Getting Pin using getter Method :", x.get_pin())
    
if __name__ == "__main__":
    main()