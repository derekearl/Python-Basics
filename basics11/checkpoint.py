# Another practice opening files

with open ('lesson11/books.txt') as books_file:
    
    #loop to display all books
    for line in books_file:

        book = line.strip()
        print (book)