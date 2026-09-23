#question see in the EMC python 10 hour crash course 1:57:37
salary=int(input("Enter your Salary:"))
age=int(input("Enter your Age:"))

if(salary>=20000 or age<=25):
    loan_amt=int(input("Required loan amount:"))
    if(loan_amt>=50000):
        print("Maximum loan amount is 50,000!")
    else:
        print("You are eligible for loan")
else:
    print("You are not eligible for loan")