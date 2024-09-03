# This is an asignment that will tell you what your grade is based on a grading scale.

grade = input('What is your grade percentage? ')
# Be sure to make the grade an int or a float because Python will need to distinguish 
# between a string and a number
grade = int(grade)

if grade >= 93:
    # Also remember when you want change the variable to a string in the print statement.
    print('Your letter grade is an A')

elif grade >= 90:
    print('Your letter grade is an A-')

elif grade >= 87:
    print ('Your letter grade is a B+')

elif grade >= 83:
    print ('Your letter grade is a B')

elif grade >= 80:
    print ('Your letter grade is a B-')

elif grade >= 77:
    print ('Your letter grade is a C+')

elif grade >= 73:
    print ('Your letter grade is a C')

elif grade >= 70:
    print ('Your letter grade is a C-')

elif grade >= 67:
    print ('Your letter grade is a D+')

elif grade >= 63:
    print ('Your letter grade is a D')

elif grade >= 60:
    print ('Your letter grade is a D-')

else:
    print ('Your letter grade is an F')

print()

gpa = input ('What was your letter grade? ')

if gpa.upper() == "A":
    print ("Your gpa is 4.0")

elif gpa.upper() == "A-":
    print ("Your gpa is 3.7")

elif gpa.upper() == "B+":
    print ("Your gpa is 3.3")

elif gpa.upper() == "B":
    print ("Your gpa is 3.0")

elif gpa.upper() == "B-":
    print ("Your gpa is 2.7")

elif gpa.upper() == "C+":
    print ("Your gpa is 2.3")

elif gpa.upper() == "C":
    print ("Your gpa is 2.0")

elif gpa.upper() == "C-":
    print ("Your gpa is 1.7")

elif gpa.upper() == "D+":
    print ("Your gpa is 1.3")

elif gpa.upper() == "D":
    print ("Your gpa is 1.0")

elif gpa.upper() == "D-":
    print ("Your gpa is 0.7")

elif gpa.upper() == "F": 
    print ('Your gpa is 0.0')

else:
    print ("Umm that is not a valid letter grade.")
    