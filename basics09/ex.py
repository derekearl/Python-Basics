# Using number in lists in python

numbers = [12.3, 13.57, 98.32, 458.786]
running_total = 0

for number in numbers:
    running_total = running_total + number
    running_total += number # Shorthand way to do this

print (f'The total is: {running_total:.2f}') # This will display 1165.95