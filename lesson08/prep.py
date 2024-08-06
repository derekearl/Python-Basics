# This lesson will introduce for loops as well

# example
items = ['Hookshot', 'Master Sword', 'Bow', 'Megaton Hammer', 'Hylian Shield']

# Items is a variable that already exists so therefore the other variable 'item'
# could be any other name you want to call it so long as it is called in the
# curly braces in the print statement
for item in items:
    print (f'The item is: {item}')

print ()

# One can create list of numbers like a list of words
    
numbers = [0,1,2,3,4,5,6,7,8,9]

# That can get to be very long and an easier way to do that would be like this
numbers = range(10)
# This will go up to ten numbers but not include number 10 because it starts with 0

for number in range(10):
    print (number)

#This loop will start with 100, and go up to 200 but not include 200
for i in range (100,200):
    print (i)

# This loop will do the same thing but will count by 10s
for i in range (100,200,10):
    print (i)

# One can make loops within a loops as well
for i in range(5):
    print (i)
    for j in range (10,13):
        print (f'--{j}')

first_name = 'Derek'
for letter in first_name:
    print (f'The letter is: {letter}')

word = input ('Type a five letter word!')
first_letter = word[0]
second_letter = word[1]
third_letter = word[2]
fourth_letter = word[3]
fifth_letter = word[4]
print (fifth_letter,fourth_letter,third_letter,second_letter,first_letter)