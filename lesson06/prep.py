# Preparation using complex conditions
# Part of the Microsoft Developer Python for Beginners Series

# If the gpa is above a 3.0 and the lowest grade 70
# They will make the honor roll

gpa = float (input('What was your Grade Point Average? '))
lowest_grade = input ('What was your lowest grade? ')
lowest_grade = int(lowest_grade)

if gpa >= 3.0 and lowest_grade >= 70:
    print ('You made the honor roll')

else:
    print ("Do not give up!")

# Here is an example of using a boolean variable to determine
# if a student made the honor roll

gpa = float (input('What was your Grade Point Average? '))
lowest_grade = input ('What was your lowest grade? ')
lowest_grade = int(lowest_grade)


if gpa >= 3.0 and lowest_grade >= 70:
    # One thing to remember is when using boolean variables
    # You need to capitilze it to work
    honor_roll = True
else:
    honor_roll = False

# We will now check to see if the condition was met

if honor_roll:
    print ('Congrats you made the honor roll!')

else:
    print ("Do not give up, Try again!")