#Create a base class called Shape with a method area that returns 0.
#Create a derived class called Rectangle that inherits from Shape 
#and overrides the area () method to calculate and return the area of a rectangle.

class Shape():
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self,l,b):
        return l * b

r1 = Rectangle()
print(r1.area(2,2))
