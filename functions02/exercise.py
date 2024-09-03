# Demo using the math.ceil() function
import math

# Get inputs from the user
items = int (input ('Enter the number of items: '))
box = int(input ("Enter the number of items per box: "))

# Calculate the formula
result = math.ceil(items/box)

# Display the results
print (f'For {items} items, packing {box} items per box you will need {result} boxes')