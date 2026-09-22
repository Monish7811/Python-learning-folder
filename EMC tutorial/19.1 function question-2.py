#2) Get a integer number from user and pass it to the function called findevenorodd().
# Let the function print whether the number is even or odd.

def findevenorodd(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")

a=int(input("Enter a number:"))
findevenorodd(a)