#3)Create a class called teacher
#Create a variable = name and register number using constructor
#Create a function called display which should display the name and register number of the teacher
#Create t1 and t2 object and pass the name and reg no value through object.

class teacher:
    def __init__(self, N, R):
        self.name = N
        self.register = R
    def display(self):
        print("Name:", self.name)
        print("Reg.No:", self.register)

#T1:
t1 = teacher("Mukesh", 1234)
#T2:
t2 = teacher("Ramesh", 4321)

t1.display()
t2.display()