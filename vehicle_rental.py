class Vehicle:
    def __init__(self,brand,model, price_per_day, avail):
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.avail = avail

    def display_details(self):
        print("\n===== VEHICLE DETAILS =====\n")
        print("Brand Name        :", self.brand)
        print("Model Name        :", self.model)
        print("Price per day     :", self.price_per_day)
        print("Availability      :", self.avail)
        
    
    def calculate_rent(self,days):
        rent = self.price_per_day * days
        print("The rent for the chosen vehicle for ", days," days is",rent,"rupees.")
        print("You can pay with Cash/UPI/Card at the payment page.")
              
    def start(self):
        print("Your ",self.brand,"with ",self.model,"is good to go.\nHave a smooth journey...") 

class Car(Vehicle):
    def __init__(self,brand,model, price_per_day, avail,engine,fuel_type):
        super().__init__(brand,model, price_per_day, avail)
        self.engine = engine
        self.fuel_type = fuel_type

    def start(self):
        print("Fasten your seat belt and have a safe journey...")

class Bike(Vehicle):
    def __init__(self,brand,model, price_per_day, avail,engine_cc,gear_type):
        super().__init__(brand,model, price_per_day, avail)
        self.engine_cc = engine_cc
        self.gear_type= gear_type

    def start(self):
        print("Buckle Up and Helmet On and don't forget to ride safe...")

car1 = Car("Toyota", "Hilux", 4500, "Available", "2.8L", "Diesel")
car2 = Car("Hyundai", "Verna", 4000, "Available", "1.5L", "Petrol")
car3 = Car("Volkswagen", "Virtus", 3500, "Available", "1.0L", "Petrol")
car4 = Car("Hyundai", "Creta", 3500, "Not Available", "1.5L", "Petrol")
car5 = Car("Toyota", "Fortuner", 5000, "Available", "2.8L", "Hybrisd")
car6 = Car("Mahindra", "ScorpioN", 5500, "Not Available", "2/2L", "Hybrid")
        
bike1 = Bike("Yamaha", "R15", 3200, "Available", 155, "Manual")
bike2 = Bike("Royal Enfield", "GT650", 3500, "Not Available", 648, "Manual")
bike3 = Bike("TVS", "Apache RTR", 2500, "Available", 160, "Manual")
bike4 = Bike("Triumph", "Speed 400", 3000, "Available", 398, "Manual")
bike5 = Bike("Honda", "H'ness CB350", 2000, "Not Available", 348, "Manual")
bike6 = Bike("Jawa", "350", 3000, "Not Available", 334, "Manual")

while True:
        print("\n===== GBU RENTALS =====\n")
        print("Welcome to GBU Rentals! Choose your preferred options :")
        print("1. Car")
        print("2. Bike")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
                print("\n===== CARS =====")
                print("1. Toyota Hilux       - ₹4500/day")
                print("2. Hyundai Verna      - ₹4000/day")
                print("3. Volkswagen Virtus  - ₹3500/day")
                print("4. Hyundai Creta      - ₹3500/day")
                print("5. Toyota Fortuner    - ₹5000/day")
                print("6. Mahindra ScorpioN  - ₹5500/day")
                
                car_choice = int(input("Enter your choice: "))
                
                if car_choice == 1:
                    selected_vehicle = car1
                elif car_choice == 2:
                    selected_vehicle = car2
                elif car_choice == 3:
                    selected_vehicle = car3
                elif car_choice == 4:
                    selected_vehicle = car4
                elif car_choice == 5:
                    selected_vehicle = car5
                elif car_choice == 6:
                    selected_vehicle = car6
                else:
                    print("Invalid vehicle choice!")
                    selected_vehicle= None
        
                if selected_vehicle is not None:
                    
                    if selected_vehicle.avail == "Available":
                        print("\nVehicle is available! Proceeding with your booking...")
                        selected_vehicle.display_details()
                        days = int(input("Enter number of days: "))
                        selected_vehicle.calculate_rent(days)
                        
                        selected_vehicle.start()
                        selected_vehicle.avail = "Not Available"
                        print("\nVehicle has been booked successfully!")
                        
                    else:
                        print("\nSorry! This vehicle is currently unavailable.",
                        "Please checkout other options.")
        
                        
        
        
        elif choice == 2:
                print("\n===== BIKES =====")
                print("1. Yamaha R15              - ₹3200/day")
                print("2. Royal Enfield GT650     - ₹3500/day")
                print("3. TVS Apache RTR          - ₹2500/day")
                print("4. Triumph Speed 400       - ₹3000/day")
                print("5. Honda H'ness CB350      - ₹2000/day")
                print("6. Jawa 350                - ₹3000/day")
                
                bike_choice = int(input("Enter your choice: "))
                
                if bike_choice == 1:
                    selected_vehicle = bike1
                elif bike_choice == 2:
                    selected_vehicle = bike2
                elif bike_choice == 3:
                    selected_vehicle = bike3
                elif bike_choice == 4:
                    selected_vehicle = bike4
                elif bike_choice == 5:
                    selected_vehicle = bike5
                elif bike_choice == 6:
                    selected_vehicle = bike6
                else:
                    print("Invalid vehicle choice!")
                    selected_vehicle = None
        
                if selected_vehicle is not None:
        
                    if selected_vehicle.avail == "Available":
                        print("Vehicle is available! Proceeding with your booking...")
                        selected_vehicle.display_details()
                        days = int(input("Enter number of days: "))
                        selected_vehicle.calculate_rent(days)
                        
                        selected_vehicle.start()
                        selected_vehicle.avail = "Not Available"
                        print("\nVehicle has been booked successfully!")
                    else:
                        print("\nSorry! This vehicle is currently unavailable.",
                        "Please checkout other options.")
        
                    
        
        elif choice == 3:
                print("Happy to serve you! Visit again.")
                break
        
        else:
            print("Invalid choice! Please try again.")
