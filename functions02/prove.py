# Prove Exercise from BYU-Idaho CSE 111 Review over basic code

# Calculating Tire Pressure from input of user
import math


width = input ('What is the width of the tire? ')
aspect = input ('What is the aspect ratio of the tire? ')
diameter = input ('What is the diameter of the tire in inches? ')

#convert the input from the user from string to int
w = int(width)
a = int(aspect)
d = int(diameter)

# Grab the formula from inside the parenthesis
z = w * a + 2540 * d
#Get the answer to the formula outside the parenthesis
y = math.pi * w ** 2 * a
# Multiply the answer inside and outside the parenthesis and divide by 10000000000
volume = z * y /10000000000

# Display the results
print (f'The approximate volume of the tire is {volume:.2f} liters')