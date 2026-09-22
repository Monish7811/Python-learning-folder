#3) Get a integer number from user and pass it to the function called findpassorfail().
#Let the function print whether the number is even or odd.

def findpassorfail(a):
    if(a>=35):
        print("Pass")
    else:
        print("Fail")

b=int(input("Enter your mark:"))

findpassorfail(b)
