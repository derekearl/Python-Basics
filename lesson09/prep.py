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
while new_items != 'quit':
    new_items = input ('What items are you buying? ')
    items.append(new_items)

for item in items:
    print(item)