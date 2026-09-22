#Question see in EMC Python 10 hour crash course in 2:12:25

print("Enter you Marks for 100:")

math=int(input("Maths:"))
science=int(input("Science:"))
tamil=int(input("Tamil:"))
social=int(input("Social:"))
english=int(input("English:"))

add=math+science+tamil+social+english
ave=add/5

if(ave<35):
    print("Additional class is required")
else:
    print("You are good to go")