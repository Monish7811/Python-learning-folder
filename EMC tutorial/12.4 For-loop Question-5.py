#Get the question from EMC 10 hour crash course in 3:15:51

count=0

for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)