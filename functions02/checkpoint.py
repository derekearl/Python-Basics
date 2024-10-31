# Demo using the math.ceil() function
import math

# Get inputs from the user
items = int(input ("Enter the number of items: "))
boxes = int(input ('Enter the number of items per box: '))

# Calculate the formula
result = math.ceil(items/boxes)

# Display the results
print (f'For {items} items, packing {boxes} in each box, you will need {result} boxes.')