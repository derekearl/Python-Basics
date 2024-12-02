# Import datetime module to use in program
from datetime import datetime

# Call now method to get current day
current_day = datetime.now()

# Call weekday method to get day of the week
# from current_day object
day = current_day.weekday()

# Display what day it is
print (day)

# Define discount rate at 10 %
discount_rate = .10
# Define Sales tax rate
tax_rate = .06

#Get the the subtotal from the user
subtotal = float(input ('What is the subtotal? '))

# Apply the discount if it is Mon or Tue
if subtotal >= 50 and (day == 1 or day == 2 ):
    print ('A 10% discount has been applied')
    discount = round (subtotal * discount_rate, 2)
    print (f'Discount amount: {discount:.2f}')
    subtotal -= discount

# Apply sales tax
sales_tax = round (subtotal * tax_rate,2)
print (f'The sales tax is {sales_tax}')

# Add the sales tax to the subtotal for the total
total = subtotal + sales_tax

# Display the total amount
print (f'The total amount is {total:.2f}')