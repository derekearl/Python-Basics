# Numbers can be stored in variables

pi = 3.14159
print (pi)

# You can also do math with python
first_num = 10
second_num = 5

print ()
# Addition example
print (first_num + second_num)
# Subtraction
print (first_num - second_num)
# Multiplication
print (first_num * second_num)
# Division
print (first_num / second_num)
# Exponent
print (first_num ** second_num)
# Divide and drop remainder
print (first_num // second_num)
# Remainder or Modulus
print (first_num % second_num)

print ()
# When displaying a string that contains numbers you must convert the numbers into strings
# Example
days_in_february = 28
print (str(days_in_february) + ' days in February') 

print()
# Numbers can be stored as strings as well
# Example
num_1 = "1"
num_2 = "2"
# If you were to use a plus sign, it would read it as a concat. The result would be just 12 

# Also remember that input functions always return strings
# You will need to use data type conversion

print()

# Exmample of data type conversion
choice_1 = input ('Choose first number: ')
choice_2 = input ('Choose second number: ')

# Example of int
print(int(choice_1) + int(choice_2))
# Example of float
print(float(choice_1) + float(choice_2))

