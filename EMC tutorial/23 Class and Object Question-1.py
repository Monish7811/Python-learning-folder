#1)Create a class called student create a variable = name and register number using constructor.
# Create a function called display which should display the name and register number of the student.
class student:
    def __init__(self):
        self.name = ""
        self.registerno = ""
    def display(self):
        print("Name:",self.name)
        print("Reg.No:",self.registerno)

#S1:
s1 = student()
s1.name = "Monish"
s1.registerno = "8507"

#S2:
s2 = student()
s2.name = "Umar"
s2.registerno = "8505"

s1.display()
s2.display()
