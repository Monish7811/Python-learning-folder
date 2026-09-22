#Get input for score out of 100
#If score < 35 print "Poor student"
#If score > 35 and score < 70 print "Average Student"
#If score > 75 print "Good student"

score=int(input("Enter your Score for 100:"))
if(score<35):
    print("Poor Student")
elif(score>35 and score<70):
    print("Average Student")
elif(score>70 and score<=100):
    print("Good Stident")
else:
    print("Invalid Score")
