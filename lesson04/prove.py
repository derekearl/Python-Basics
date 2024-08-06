import math

# Prove assignment for adult meal, kid meal, subtotal, tax, and grand total

# I usually code in single quotes for python but this time I will use double
# quotes because there will be an apostrophe in this example

child_meal = input ("What is the price of a child's meal? ")
adult_meal = input ("What is the price of a adults's meal? ")
children = input ("How many children are there? ")
adults = input ("How many adults are there? ")
tax = input ("What percent is the tax rate? ")

print ()

# The best way to get a subtotal is to multiply the price of a child's meal by the number of children there are
# and multiply the price of an adult's meal by the number of adults there are and them together.
subtotal = (float (child_meal) * int (children) + float(adult_meal) * int(adults))
print (f"The Subtotal is: {subtotal:.2f}")
# In order to get a sales tax first divide the tax percent by 100 then multiply it by the subtotal.
sales_tax = (float (tax) / 100) * subtotal
print (f"The sales tax is: {sales_tax:.2f}")
# To get the total just add the sales tax and the subtotal together.
total = sales_tax + subtotal
print (f"The total is: {total:.2f}")

print ()

payment = input ("What is the payment amount? ")
# In order to calculate change just subtract the total from the payment.
change = (float (payment) - float (total))
print (f"Your change is: {change:.2f}")