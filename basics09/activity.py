# List of numbers exercise

print ('Enter a list of numbers, type 0 when finished')

numbers = []
number = -1

while number != 0:
    number = int(input('Enter Number: '))

    if number != 0:
        numbers.append(number)


sum = 0

for number in numbers:
    sum += number

print (f'The sum is: {sum}')

count = len(numbers)
average = sum / count

best_so_far = -1
for number in numbers:
    if number > best_so_far:
        best_so_far = number

print (f'The largest number is: {best_so_far}')

smallest_so_far = 99999999

for number in numbers:
    if number > 0 and number < smallest_so_far:
        smallest_so_far = number

print (f'The smallest number is: {smallest_so_far}')

sorted_list =sorted(numbers)

print ('The sorted list is:')
for number in sorted_list:
    print(number)