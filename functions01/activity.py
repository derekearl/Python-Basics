# Activity determining the swing of a pendulum
# BYU-Idaho CSE 111 Week 1 Teach Activity

import math

# Get the height of the pendulum and convert to float
h = float (input ('How long is the pendulum in meters? '))

# Calculate the formula
time = 2 * math.pi * math.sqrt (h / 9.81)

# Display the results
print (f'The time that it takes to swing back and forth is: \n'
       f'{time:.2f} seconds.')
