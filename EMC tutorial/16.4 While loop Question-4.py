#4) write a program to find the factorial of a number.

i=int(input())
fact=1 # This variable stores the running total

while(i>1):  # The loop will run as long as i is greater than 1
    fact=fact*i  # Multiply the current total by i
    i=i-1  # Decrease i by 1 (5 -> 4 -> 3 -> 2)
print(fact)  # Output