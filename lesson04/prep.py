# This is going to show rounding options

cars = 3
people = 8

people_per_car = people / cars

# Round to 1 decimal
print(f'There are {people_per_car:.1f} people in each car.')
# The output will display 2.7 people in each car

# Round to 2 decimals
print(f'There are {people_per_car:.2f} people in each car.')
# The output will display 2.67 people in each car

# Round to 3 decimas
print(f'There are {people_per_car:.3f} people in each car.')
# The output will display 2.667 people in each car

print()

# Scientific notation example
distance = 9 * 1205 * 18

# Scientific notation with 3 digits of precision
print (f'The distance is: {distance:.3e} meters.')
# The output will be 1.952e+05 meters

# Scientific notation with 6 digits of precision
print (f'The distance is: {distance:.6e} meters')
# The output will be 1.952100e+05 meters

print()

# The next exampel will display thousands grouping

big_number = 123456789

# Display without formatting
print (f'The number is: {big_number}')
# The output will display 123456789 no commas or underscores

# Display with "," formatting
print (f'The number is: {big_number:,}')
# The output will display commas between every thousandth position

# Display with "_" formatting
print (f'The number is: {big_number:_}')
# The output will display underscores between every thousandth position
