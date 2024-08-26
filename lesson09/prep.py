# This lesson is about using lists in python

# In order to make a list you use a name and = []
students = ['Garrett', 'Derek', 'John']
print (students)
print()

# You can also add more items to your list as well
students.append('Arthur')
# This will add the name Arthur to our list
print (students)
print()

# Demo using a for loop
for student in students:
    print (student)
print()

# You can get an input from a user and add the item to a list as well
new_student = input ('What is the name of the new student? ')
students.append(new_student)
print (students)
print()

# You can also add some names until you don't want to using a while loop
items = []
new_items = ''

# Use while loop to add items or type quit
while new_items != 'quit':
    new_items = input ('What items are you buying? ')

    # Will not add the word quit to the list.
    if new_items != 'quit':
        #adds items to the list
        items.append(new_items)

print()
print ('The Items you added are: ')

for item in items:
    print (item)