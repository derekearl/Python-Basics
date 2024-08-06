# It is important to remember that string comparisons are case sensitive
# Here is an example to overcome that.

country = input ('What country are you from? ')
if country.lower() == 'america':
    print ('Do you like baseball or football better?')
else:
    print ('What country are you from? ')

# It will not matter if you use upper, lower, or even mixed case, Python will recognize it!