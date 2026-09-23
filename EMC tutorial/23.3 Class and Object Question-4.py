#4)Create a class called calculator
#Create 2 variables a and b
#Create a function called add,sub,mul,div all functions should take 2 variables as parameter:
#Pass the a and b value through object().

class Calculator:
    def __init__(self,a,b):
        self.num1 = a
        self.num2 = b
    def add(self):
        print("Add:",self.num1+self.num2)
    def sub(self):
        print("Sub:",self.num1-self.num2)
    def mul(self):
        print("Mul:",self.num1*self.num2)
    def div(self):
        print("Div",self.num1/self.num2)

obj1 = Calculator(10,5)
obj1.add()
obj1.sub()
obj1.mul()
obj1.div()
