# This is extra work that is covered in the Microsoft Developer 
# videos but not in the class this is just to better understand
# collections and such

# examples

# To set up a list in Python you use square brackets []
names = ['Derek', 'Garrett']
scores = []
scores.append(98) # Add new item to the end 
scores.append(99) 
print (names)
print (scores)
print (scores[1]) 
# Collections are zero-indexed: meaning that 0 is 1
# 1 is 2, 2 is 3, etc


# In this case it is calling the scores list and it is going
# to display the second number which is 99

# Another demonstration on this with a print statement

print ("My name is " +str(names[0]))
print ('My best friend is ' + str(names[1]))

print ()

# Demos with lists and common operations
print(len(names)) # This will get the number of items
names.insert(0, "Gandalf") # Will inser this before index
print (names)
names.sort() # Sorts the names in alphbetical order
print (names) # Displays the names in alphbetical order

# You can retrieve ranges from lists
fellowship = ['Boromir', 'Aragorn', 'Legolas', 'Merry', 'Pippin', 'Gimili','Frodo', 'Sam']
survivors = fellowship[1:7]
# Start an end Index

print (fellowship)
print (survivors)

# Here is some examples of Dictionaries
person = {'first': 'Derek'}
person['last'] = 'Earl'
print (person)
print (person ['first'])