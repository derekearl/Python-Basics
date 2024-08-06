# This comes from lesson 10 using lists to solve problems


the_list = ['item1', 'item2', 'item3']
# You can access an item in a list at a given index via the square bracket [] notation:
first = the_list[0] # gets the first item
second = the_list[1] # gets the second item

index = int(input ("Which index would you like to get? "))
user_choice = the_list[index] # gets the item at the index the user typed

print()

books = ["The Lord of the Rings", "The Last Wish", "The Way of Kings"]
# You can find of the number of elements in a list as well
number_of_books = len(books)

# The previous lesson showed how to iterate through each item in a list
# using a for loop. You can also have the loop iterate through the indexes
# 0 through the size of the lists, and access them using [] notation.
for i in range(len(books)):
    book = books[i]
    print(book) # This will print out each book.

# If you want to print the index numbers next to the elements you can do this
for i in range(len(books)):
    book = books[i]
    print(f'{i}. {book}')

print()

# Working with parallel lists: sometimes you want to display elements beside other elements
# For example, contact info like in your phone
names = ['Derek', 'Garrett']
numbers = ['1017', '1103']

# The best way to do this is to loop through the indexes that correspond
# to one of the lists and then access tem from each list at the index.
for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f'{name} - {number}')

print()

# You can also remove items from a list. The best way to do that is to use the 'pop' function
the_list.pop(2) # Will remove the item at index 2
the_list.pop() # Will just removes the last item (In this case item2 will be removed)
print(the_list)