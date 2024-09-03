# Week 10 prove assignment making a shopping cart program

print ('Welcome to the shopping cart program')

items = []
new_items = ''
prices = []
input ('Press enter to bring up main menu: ')
while input != 5:
    print()
    print ('1. Add Item')
    print ('2. View Cart')
    print ('3. Remove Item')
    print ('4. Compute total')
    print ('5. Quit')
    choice = int(input ('Which of the following would you like to do? '))

    if choice == 1:
        #print ('Add what ever you would like to the list, type done to stop.')
        new_items = input ('What item would you like to add? ')

        if new_items != 'done':
                items.append(new_items)
                price = float(input ('How much does the item cost? '))
                prices.append(price)
        print (f'{items} has been added to the cart. ')

    elif choice == 2:
        print ('The contents of the cart are:')
        for i in range(len(items)):
            item = items[i]
            price = prices[i]


            print (f'{item} - {price:.2f}')

    elif choice == 3:
        item_number = int(input("Which item would you like to remove? "))
        index = item_number - 1
        
        if 0 <= index < len(items):
            items.pop(index)
            prices.pop(index)
            print("Item removed.")
        else:
            print("Sorry, that is not a valid item number.")
         

    elif choice == 4:
        print(f'The total price of the contents are: {sum(prices):.2f}')

    else:
        print ('Thank You come again!')
        break