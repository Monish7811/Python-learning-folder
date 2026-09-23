#2)Create a class called Fruit Create a variable called color using _init_method.
#Create a object called apple "Pass the color variable as a parameter through object".

class fruit:
    def __init__(self,col):
        self.color = col

apple = fruit("red")
print(apple.color)
