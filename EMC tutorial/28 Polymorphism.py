#The word polymorphism means having many forms. In programming,
#polymorphism means the same function name (but different signatures) being used for different types. 
#The key difference is the data types and number of arguments used in function.

def add(a,b,c=0):
    print(a+b+c)

add(1,2)
add(1,2,3)