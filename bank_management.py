class Bank:
    def __init__(self, name, acc_no, access_pin):
        self.name= name
        self.acc_no = acc_no
        self.access_pin = access_pin
        self.__balance = 0
    
    def deposit(self):
       
        amount = int(input("Enter depositing amount : "))

        if amount<=0 :
            print("Invalid amount entered! Please try again.")
        else:
            self.__balance += amount
            print("Money deposited successfully \nThank you for using our services.")

    def withdraw(self):
        
        amount = int(input("Enter withdrawal amount : "))

        if amount>0 :
            if self.__balance >= amount:
                self.__balance -=amount
                print("Collect your money \nThank you for using our services.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount entered! Please try again.")

    def check_balance(self):
        print("Current Balance : ",self.__balance)

    def display_details(self):
        
        print("\n===== ACCOUNT DETAILS =====")
        print("Name         :", self.name)
        print("Account No.  :", self.acc_no)
        print("Balance      :", self.__balance)
        

name = input("Enter Account holder name : ")
print("Hello ",name,"! Enter your details below...")
acc_no= int(input("Enter you Account number : "))
access_pin = int(input("Enter your PIN : "))

cust1 = Bank(name,acc_no,access_pin)

while True:
    print("\n===== GBU BANK =====\n")
    print("Welcome to GBU Bank! Check out our services below :")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cust1.deposit()

    elif choice == 2:
        cust1.withdraw()

    elif choice == 3:
        cust1.check_balance()

    elif choice == 4:
        cust1.display_details()

    elif choice == 5:
        print("Thank you for using GBU Bank, Have a nice day!")
        break

    else:
        print("Invalid choice! Please try again.")
