# Example of using loops in a real world setting

tip = float(input ('What is your tip amount? '))

while tip < 0:
    # Leaving a negative tip does not make sense
    # The server cannot pay you for eating
    print ('Sorry, the tip cannot be negative')
    tip = float(input ('What is your tip amount? '))

print (f'Your tip amount is: ${tip:.2f}')
    