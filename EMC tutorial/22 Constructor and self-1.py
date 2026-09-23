#A constructor is a unique function that gets called automatically when an object is created of a class.
#The main purpose of a constructor is to initialize or assign values to the data members of that class.

class laptop:
    def __init__(self): #__init__ is a constructor (a in-built function) so it will automatically when i assign an object to t5he class
        self.name = ""
        self.ram = ""
        self.processor = ""
    def display(self):
        print(self.name)
        print("ram:",self.ram) #self is used to denote the current object (eg, here iam using self.ram, Python will take this as hp.ram because im using hp to call the function display)
        print("processor:",self.processor)

#Hp:
hp = laptop()
hp.name = "HP:"
hp.ram = "8gb"
hp.processor = "i5"

#Dell:
dell = laptop()
dell.name = "Dell:"
dell.ram = "16gb"
dell.processor = "i7"

hp.display()
dell.display()