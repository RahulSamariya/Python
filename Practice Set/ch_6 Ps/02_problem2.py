marks1  = int(input("Enter your marks in Physics: "))
marks2  = int(input("Enter your marks in Maths: "))
marks3  = int(input("Enter your marks in Chemistry: "))

# check for total percentage
total_percentage = ((marks1 + marks2 + marks3) / 3) 

if (total_percentage >= 40):
    print("you are pass:" , int(total_percentage),"%")
    print("Very Good")

else:
    print("you failed , better luck next time" , total_percentage)
