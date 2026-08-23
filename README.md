# Python OOP Projects

A collection of beginner-level Python projects created to practice and understand Object-Oriented Programming (OOP) concepts.

## Projects

### 1. Student Management System

A simple program that takes student details and marks, then calculates the total marks, percentage, grade, and final result.

**Concepts used:**
- Classes and Objects
- Constructor
- Instance Variables
- Methods
- Conditional Statements

**Basic Flow:**

Student Details → Enter Marks → Create Student Object → Calculate Total → Calculate Percentage → Calculate Grade → Check Result → Display Result

---

### 2. Bank Management System

A basic banking system that allows the user to perform common banking operations.

**Features:**
- Deposit money
- Withdraw money
- Check balance
- Display account details
- Exit

**Concepts used:**
- Classes and Objects
- Constructor
- Methods
- Encapsulation
- Private Attributes
- `while` loop
- Conditional Statements

**Basic Flow:**

Create Account → Display Menu → Choose Operation → Perform Operation → Return to Menu → Exit

The account balance is stored as a private attribute using `__balance`.

---

### 3. Vehicle Rental System

A simple vehicle rental system where users can choose between cars and bikes, check availability, calculate rent, and book a vehicle.

**Features:**
- Car selection
- Bike selection
- Vehicle details
- Availability checking
- Rental cost calculation
- Vehicle booking

**Concepts used:**
- Classes and Objects
- Inheritance
- Constructor
- `super()`
- Method Overriding
- Polymorphism

**Class Structure:**

Vehicle  
├── Car  
└── Bike

The `Car` and `Bike` classes inherit common properties from the `Vehicle` class and override the `start()` method with their own behaviour.

**Basic Flow:**

Choose Vehicle Type → Select Vehicle → Check Availability → Enter Rental Days → Calculate Rent → Start Vehicle → Book Vehicle

---

### 4. Simple Payment System

A basic payment system demonstrating different payment methods using inheritance and polymorphism.

**Payment Methods:**
- Cash
- UPI
- Card

**Concepts used:**
- Classes and Objects
- Inheritance
- Constructor
- `super()`
- Method Overriding
- Polymorphism

**Class Structure:**

Payment  
├── Cash_payment  
├── UPI_payment  
└── Card_payment

Each payment class provides its own implementation of the `pay()` method.

**Basic Flow:**

Enter Amount → Choose Payment Method → Create Payment Object → Select Payment → Call `pay()`

The same `pay()` method behaves differently depending on the selected payment object, demonstrating polymorphism.

---

## OOP Concepts Covered

| Concept | Project |
|---|---|
| Classes & Objects | All Projects |
| Constructors | All Projects |
| Methods | All Projects |
| Encapsulation | Bank Management System |
| Inheritance | Vehicle Rental, Payment System |
| `super()` | Vehicle Rental, Payment System |
| Method Overriding | Vehicle Rental, Payment System |
| Polymorphism | Vehicle Rental, Payment System |

## Technologies Used

- Python
- Jupyter Notebook

No external libraries are required.

## Purpose

These projects were created as beginner-level practice while learning Python Object-Oriented Programming.

The main goal was to understand OOP concepts by applying them to simple real-world examples.

## Future Improvements

- Better input validation
- Exception handling
- File handling
- Database integration
- Improved user interface
- More advanced OOP structure

## Author

**Sudip Mondal**
