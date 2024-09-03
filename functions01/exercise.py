# Demo asking a user for input and applying built-in functions
# Exercise 1 week 1 BYU- Idaho CSE 111

# Get the input from the user (Age)
answer = input ('What is your age? ')

# Convert string into an interger
age = int(answer)

# Calculate slowest and fastest possible heart rate
# Subtract age from 220 and multiply .65 for lowest
# and .85 for the highest
max_rate = 220 - age
slowest_rate = max_rate * .65
fastest_rate = max_rate * .85

# Display the results
print ()
print (f"Your highest heart rate when exercising should be {fastest_rate:.0f} beats per minute \n"
       f"and your lowest rate should be {slowest_rate:.0f} beats per minute ")