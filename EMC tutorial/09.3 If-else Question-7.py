#Get input for score percentage. Only if the percentage is greater than 70,get input for name,department and location. Then print you are eligible. If not print you are not eligible.
score=int(input("Score Percentage:"))

if(score>=70):
    name=input("Enter your Name:")
    department=input("Enter your Department:")
    location=input("Enter your location:")
    print("You are eligible")
else:
    print("You are not eligible")