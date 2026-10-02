#Create a class called Animal with a method sound() that prints "Animal makes a sound."
#Create a derived class called Dog that inherits from Animal and overrides the sound () method to print "Dog barks."
#Create another derived class called Bird that inherits from Animal and overrides the sound () method to print "Birds Sing."

class animal():
    def sound(self):
        print("Animal makes a sound.")

class dog(animal):
    def sound(self):
        print("Dog barks")

class bird(animal):
    def sound(self):
        print("Bird sings")

d1 = dog()
d1.sound()

b1 = bird()
b1.sound()