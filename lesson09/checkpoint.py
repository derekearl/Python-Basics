# Adding names of friends to a list

# Start of by creating an empty list
friends = []

name = None

while name != 'end':
    name = input ('Please enter the name of a friend: ')

    # This code must be included, otherwise the word end will be added to the list
    if name != 'end':
        friends.append(name)

print ()
print ('Your friends are: ')

for friend in friends:
    print (friend)