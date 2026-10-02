#Create a base class called Person with a constructor that takes a name as a parameter.
#Create a derived class called Student that inherits from Person and has a constructor that takes a parameter called grade. 
#Write a method in Student to display the name and grade of the student. Use Super Keyword to achieve this.

class Person():
    def __init__(self,name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def display(self):
        print(self.name,self.grade)

s1 = Student("Monish", "A")
s1.display()