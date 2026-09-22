#Get the question from EMC 10 hour crash course in 3:15:51

count_even=0
count_odd=0

for i in range(1,11):
    if(i%2==0):
        count_even=count_even+1
    else:
        count_odd=count_odd+1

print("Even:",count_even)
print("Odd:",count_odd)