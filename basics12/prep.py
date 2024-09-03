# This exercise demostrates code by finding the biggest number

# Create a list of numbers
numbers = [3, 78, 94, 23, 55, 10, 48, 88, 100]


largest_so_far = numbers[0]

# Loop through all the numbers
for number in numbers:
    if number > largest_so_far:

        largest_so_far = number # finds the largest number in the list

# Loop is done and can now display the biggest number.
print (f'The largest number so far is: {largest_so_far}')