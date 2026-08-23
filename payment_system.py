class Payment:
    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print("Processing your Transaction...")
        
class Cash_payment(Payment):
    def __init__(self,amount):
        super().__init__(amount)
    def pay(self):
        print("You can visit the counter for cash payment.",
              "\nThank you for using our services.")

class UPI_payment(Payment):
    def __init__(self,amount,upi_id,pin):
        super().__init__(amount)
        self.upi_id= upi_id
        self.pin= pin

    def pay(self):
        print("Taking you to the UPI payment page.")
        
class Card_payment(Payment):
    def __init__(self,amount,name,last_digits,cvv):
        super().__init__(amount)
        self.name= name
        self.last_digits= last_digits
        self.cvv=cvv

    def pay(self):
        print("Taking you to the Card payment page.")


amount= int(input("Enter Transaction amount :"))
print("\n===== GBU PAYMENT PORTAL =====\n")
print("Choose the method of transaction :")
print("1. Cash")
print("2. UPI")
print("3. Card(Debit/Credit)")


choice = int(input("Enter your choice: "))
        
if choice == 1:
    cash1= Cash_payment(amount)
    selected_payment = cash1
    selected_payment.pay()

elif choice == 2:
    upi_id = input("Enter valid UPI/VPA id :")
    pin = int(input("Enter your UPI pin :"))
    upi1= UPI_payment(amount,upi_id,pin)
    selected_payment = upi1
    selected_payment.pay()

elif choice == 3:
    name = input("Enter your Card holder's name :")
    last_digits =int(input("Hello ", name, "! Enter your card's last 4 digits :"))
    cvv = int(input("Enter cvv :"))
    card1= Card_payment(amount,name,last_digits,cvv)
    selected_payment = card1
    selected_payment.pay()
        
else:
    print("Invalid choice entered. Please try again...")
