#Create a Mini Calculator

a=int(input("Enter First Number:"))
b=int(input("Enter Secind Number:"))

operation=input("add/sub/mul/div:")

if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print("Invalid operation")
