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
        
        
    def menu(self):
        while True:
            print("\n=== ATM Menu for Account", self.account_id, "===")
            print("1. Create Pin")
            print("2. Check Balance")
            print("3. Withdraw Money")
            print("4. Deposit Money")
            print("5. Return to Main Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.create_pin()
            elif choice == "2":
                self.check_balance()
            elif choice == "3":
                self.withdraw_money()
            elif choice == "4":
                self.deposit_money()
            elif choice == "5":
                print(f"Returning to main menu from Account {self.account_id}")
                break
            else:
                print("Invalid choice. Please try again")


        
        
    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin created successfully")
        
    def check_balance(self):
        temp_pin = input("Enter your pin: ")
        if temp_pin == self.pin:
            print("Your balance is:", self.balance)
        else:
            print("Invalid pin")
            
    def withdraw_money(self):
        temp_pin = input("Enter your pin: ")
        if temp_pin == self.pin:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Amount withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")
            
    def deposit_money(self):
        temp_pin = input("Enter your pin: ")
        if temp_pin == self.pin:
            amount = int(input("Enter the amount to deposit: "))
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid pin")

def main():
    
    
    
    x = ATM()
    x.set_pin("656565")
    print("Getting Pin using getter Method :", x.get_pin())
    
    # accounts = {}
    
    # while True:
    #     print("\n=== Main Menu ===")
        # print("1. Create New ATM Account")
        # print("2. Access Existing Account")
        # print("3. Exit Program")
        
        # choice = input("Enter your choice: ")
        
        # if choice == "1":
        #     account_id = input("Enter a unique account ID: ")
        #     if account_id in accounts:
        #         print("Account ID already exists!")
        #     else:
        #         accounts[account_id] = ATM(account_id)
        
        # elif choice == "2":
        #     if not accounts:
        #         print("No accounts exist yet. Please create an account first.")
        #         continue
                
        #     print("\nExisting accounts:", list(accounts.values()))
        #     account_id = input("Enter account ID to access: ")
        #     if account_id in accounts:
        #         accounts[account_id].menu()
        #     else:
        #         print("Account not found!")
        
        # elif choice == "3":
        #     print("Thank you for using the ATM system. Goodbye!")
        #     break
            
        # else:
        #     print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()