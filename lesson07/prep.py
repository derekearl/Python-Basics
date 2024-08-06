# Here is prep work for working with loops

# Basic understanding of Loops
number = 0 

while number < 10:
    number = int(input ('What is the number?'))

print ("Finished with Loop!")

number = 1

while number <= 5:
    # Display the number
    print(f'The number is: {number}')

    # Update the number by adding 1 to previous number
    number = number + 1

print ('Finished with Loop!')


# Be sure to set a variable to a value in this case
# It is wise to set the number to something like 0 or 1
# rather than like 6 or anything random. Also if you were
# to set the number variable to something greater than 10
# in this case it would return an error.
number = 0

while number < 10:
    number = int(input('What is the number? '))

print ('Finished with the loop!')

# Example using a name declared as a variable before the loop
number = 0
# It is best to leave this as an empty string because we will
# ask what the user's name is below.
name = ''

while number < 10:
    number = int(input ('What is the number? '))
    name = input ('What is your name? ')

print (f'Your name is: {name}')

