# This is a demonstration of lists

# To make declare a list, you use brackets
# To make an empty lists do this,
example = []

# you can make a list with items already in it.
shows = ["Naruto", "Breaking Bad", "The Witcher"]
# You can also use numbers in a lists as well
scores = [87.7, 72.4, 99.9, 20.8]


# Here is how to add items to a list
books = []

books.append("CompTIA")
books.append("The Lord of the Rings")
books.append("Warhammer 40K")

# Iterate through the list
print ("Your books are: ")
for book in books:
    print (book)

age = 30
age = age + 1
print (age) # This will display 31

# Here is a shorthand way to do it
number = 45
number += 1
print (number) # This will display 46