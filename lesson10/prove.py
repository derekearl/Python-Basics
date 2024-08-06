# Week 10 prove assignment making a shopping cart program

print ('Welcome to the shopping cart program')

items = []
prices = []
new_items = ''
while new_items == True:
    print()
    print ('Please select one of the following: ')
    print ('1. Add Item')
    print ('2. View Cart')
    print ('3. Remove Item')
    print ('4. Compute total')
    print ('5. Quit')
    choice = int(input ('Which of the following would you like to do? '))

    if choice == 1:
        items = input ('What item would you like to add? ')
        items.append(new_items)
        price = float(input ('How much does the item cost? '))
        prices.append(price)
        print (f'{items} has been added to the cart. ')

    elif choice == 2:
        print ('The contents in the shopping cart are:')
        for item in items:
            #count = item + 1
            #item = items[i]
            #price = prices[i]
            print (item)
            