# Extra practice using a list and different functions

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

# Start the age at something very high
youngest_age = 999

# All this does is keep track of person with the youngest age
# Use an empty string
youngest_person = ''

# Go through each person in the list
for person in people:

    parts = person.split() # splits on the space

    # Set variables
    name = parts[0]
    age = int( parts[1])

    # This will check to see if the person is younger
    # than the one before
    if age < youngest_age:

        # Save name and age as the youngest
        youngest_age = age
        youngest_person = name

# The loop is done so now we print the statement.
print (f'The youngest person on the list is {youngest_person} who is {youngest_age} years old')