class Student:
    def __init__(self,name, roll_no,dbms,programming,lab):
        self.name = name
        self.roll_no = roll_no
        self.dbms = dbms
        self.programming = programming
        self.lab = lab

    def calculate_total(self):
        return self.dbms+self.programming+self.lab

    def calculate_percentage(self):
        return (self.calculate_total()/300)*100

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def check_result(self):
        if self.dbms >= 33 and self.programming>=33 and self.lab>=33 :
            return "Congrats ! You've cleared the exam."
        else :
            return "Alas ! You've failed for this attempt."

    def display_details(self):
        print("\n===== STUDENT RESULT =====")
        print("Name        :", self.name)
        print("Roll Number :", self.roll_no)
        print("DBMS        :", self.dbms)
        print("Programming :", self.programming)
        print("Lab         :", self.lab)
        print("Total       :", self.calculate_total())
        print("Percentage  :", self.calculate_percentage(), "%")
        print("Grade       :", self.calculate_grade())
        print("Result      :", self.check_result())

name = input("Enter Student name : ")
roll_no = int(input("Enter your Roll number : "))
print("Hello ",name,"! Enter your marks below...")
dbms = float(input("Enter Database Management marks: "))
programming = float(input("Enter Programming marks: "))
lab = float(input("Enter Lab marks: "))

student1 = Student(name,roll_no,dbms, programming, lab)
student1.display_details()
