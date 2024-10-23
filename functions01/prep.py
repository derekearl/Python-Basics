# This is just a review of past things using boolean, variables, ints, floats, etc

a = "My name is " # string
b = "Derek" # string
c = a + b # string and a string makes a string
print (f"a: {type(a)} {a}")
print (f"a: {type(b)} {b}")
print (f"a: {type(c)} {c}")
print ()

d = False # boolean
e = True # boolean
print (f'd: {type(d)} {d}')
print (f'e: {type(e)} {e}')
print ()

f = 15 # int
g = 7.54 # float
h = f + g # int plus float equals float
print (f'f: {type(f)} {f}')
print (f'g: {type(h)} {h}')
print (f'h: {type(h)} {h}')
print ()

i = "True" # This is a string becasue of the quotes
j = "4.52" # Even though this is a number it is also a string because of quotes
print (f'i: {type(i)} {i}')
print (f'i: {type(i)} {i}')

# Further Examples
# The input function will always return a string

k = input ('Please enter a number: ')
l = input ('Please enter another number: ')
m = k + l  # String plus a string equals a string

print (f'k: {type(k)} {k}')
print (f'l: {type(l)} {l}')
print (f'm: {type(m)} {m}') # This will display the first and second number combined

# Convert the functions to int and float

n = int(input('Please enter a whole number: '))
o = float(input('Please enter a decimal number: '))
p = n + o

print(f"n: {type(n)} {n}")
print(f"o: {type(o)} {o}")
print(f"p: {type(p)} {p}")

# Another Example

# Given the distance that a cable will span and the distance
# it will sag or dip in the middle, this program computes the
# length of the cable.

# Get user input and convert it from
# strings to floating point numbers.
span = float(input("Distance the cable must span in meters: "))
dip = float(input("Distance the cable will sag in meters: "))

# Use the numbers to compute the cable length.
length = span + (8 * dip**2) / (3 * span)

# Print the cable length in the
# console window for the user to see.
print(f"Length of cable in meters: {length:.2f}")




