# Review of calling functions.  BYU-Idaho CSE 111

name = input ('Please enter a name: ')
print (f'Hello {name}')

# To call a function you need to know the following:
# 1. Name of the function
# 2. The parameters that the function accepts
# 3. What the function does

# This is how it works from the function above

# The name of the function is input.
# The function accepts one parameter named prompt.
# The function writes the prompt to a terminal window and then reads
# user input from the terminal and returns that input to the calling function.

# A parameter is a piece of data that a function needs in order to complete its task. 
# In the online reference for the input function, we see that the input function has one parameter named prompt.

# An argument is the value that is passed through a parameter into a function. In other words, parameters 
# are listed in a function’s documentation, and arguments are listed in a call to a function.

# Another example
n = float (input ('Enter a number: '))
r = round(n, 2)
print (r)

# Example rounding a float to a whole number

number = float (input ("Enter a number with a decimal: "))
near = round(number)
print (near)

# Named Arguments are preceded by the name of the matching parameter

x = "One"
y = "Two"
z = "Three"
print(x, y, z, sep="|", flush=True)

# Calling a Function inside a Module
# Python standard library has many functions like the math module
# This includes functions like the floor, ceil, sqrt functions.
# There is also the random module which has functions like
# randint, choice, and shuffle.

# Example
# Usually I would put import math at the top of the page but for the
# sake of this example I am going to put it here.
import math

ex = math.sqrt(81)
print (ex)

# In the example above we have the following
# 1. The name of the module is math
# 2. The name of the function is sqrt
# 3. The function accepts one parameter which is 81
# 4. The function computes and returns the square root of 81

# Calling a Method
# A Method is just a function that belongs to a class or object

# Example

# Start by getting a string of text
text1 = input ('Enter your favorite quote: ')

# Call built in len function to get the number of characters
length = len(text1)

# Call string "Upper" method to make quote all caps
text2 = text1.upper()

# Call the print function to display the number of characters
print (text2, length)

# Retruning a stored value

#Example 

# Get a number
number1 = float (input ('Enter a number: '))

# Call the sqrt function and print the return value
print (math.sqrt(number1))

# Call the sqrt function use the value in an if statement
if math.sqrt(number1) < 100:
    print (f'The sqaure root is less than 100')
elif math.sqrt(number1) > 100:
    print (f'The square root is more than 100')
else:
    print (f'The sqaure root is 100')

# Final Example

# Get another number from the user
number2 = float(input ('Enter another number: '))

# Call the sqrt function and store its return value
root = math.sqrt(number2)

print (f'The saqure root of the number is: {root:.2f}')

# Use if-then statement like in the last example
if root < 100:
    print (f'The squre root is less than 100')
elif root > 100:
    print (f'The sqare root is greater than 100')
else:
    print ('The sqaure root is exactly 100')