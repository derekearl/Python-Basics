# print('push ctrl + kc to comment out this line, and ctrl + ku to uncomment this line')


# strings and can be stored in variables
# comment the next two lines when not in use
#first_name = 'Derek'
#print (first_name)

# combining strings
first_name = 'Derek'
last_name = 'Earl'



print()
#comment the lines when not in use for program to run smoothly
# This will display DerekEarl
print(first_name + last_name)
#This will display Hello Derek Earl
print('Hello ' + first_name + ' ' + last_name)

print()
sentence = 'zelda series is the best'
#displays all capital letters
print(sentence.upper())
#displays all lowercase letters
print(sentence.lower())
# capitalizes the first letter
print(sentence.capitalize())
# displays the number of times a certain letter appears
#try putting in another letter such as z or x
print(sentence.count('s'))

# Functions help us format strings we save  to files and databases, or display to users
first_name = input ('What is your first name? ')
last_name = input ('What is your last name? ')
# You can try sawpping out capitalize with stuff like upper, lower, or count how many letters are in the string.
print ('Hello, ' + first_name.capitalize() + ' ' + last_name.capitalize()) 
# Here are some other ways that you can make the same display
#output = 'Hello, ' + first_name + ' ' + last_name
# output = 'Hello, {} {}'.format(first_name, last_name)
# keep in mind that if you will swap the 1 and 0 around it will display the last name first.
# output = 'Hello, {0} {1}'.format(first_name, last_name)
# # This is only available in python3
output = f'Hello, {first_name} {last_name}'

print (output)


