#6)(a+b)*c
#Get input for a and b and function called add() which should return the sum of a and b
#And multiply that sum with c

def add(n1,n2):
    return n1+n2

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

added=add(a,b)
output=added*c

print(output)