# Demo asking a user for input and applying built-in functions
# Exercise 1 week 1 BYU- Idaho CSE 111

# Get the input from the user (Age)
answer = input ('What is your current age? ')

# Convert string into an interger
age = int(answer)

# Calculate slowest and fastest possible heart rate
# Subtract age from 220 and multiply .65 for lowest
# and .85 for the highest
highest = (220 - age) * .85
lowest = (220 - age) * .65 

# Display the results
print ()
print (f'Your highest heart rate should be: {highest:.0f}\n'
       f'Your lowest heart rate should be: {lowest:.0f}')