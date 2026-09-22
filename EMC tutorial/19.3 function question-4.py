#4)Get input for a and b and pass it to the function called printrange() let
#the function print numbers from a to b.

def printrange(r1,r2):
    for i in range(r1,r2+1):
        print(i)

a=int(input("Enter num1:"))
b=int(input("Enter num2:"))

printrange(a,b)