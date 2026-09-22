a=[]
print("Enter 10 Numbers:")
for i in range(10):
    num=int(input("Enter Number "+str(i+1)))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i

print(sum)