# This is just extra work from the Microsoft Developer Channel not required work
# from Brigham Young University-Idaho. I felt it was important to include this.

x = 42
y = 0

print ()
try:
    print (x/y)
except ZeroDivisionError as e:
    print ("Not allowed to Divide by Zero")
else:
    print ('Something else went wrong.')
finally:
    print ('This is cleanup code')
print ()