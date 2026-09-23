#5)Set s_username="EMC" s_password="123"
#Get input for uname and password
#Create a function called validate.
#If uname and password matches the function should return true else false.


s_username="Monish"
s_password="monish7811"

uname=input("Enter your Username:")
password=input("Enter your Password:")

def validate():
    if(uname == s_username and password == s_password):
        return True
    else:
        return False

a=validate()
print(a)