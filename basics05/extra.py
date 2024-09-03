# This is extra work from the series of videos by Microsoft Developer used in the
# Programming Buidling Blocks Class

# Dates
# To get current date and time we need to use the datetime library
from datetime import datetime, timedelta

today = datetime.now()
# This function will return a datetime object
print ('Today is:' + str(today))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print ('Yesterday was:' + str(yesterday))

print ()

# This will display the day, month, year, hour, minute, and second
print ('Day:' + str(today.day))
print ('Month:' + str(today.month))
print ('Year:' + str(today.year))
print ('Hour:' + str(today.hour))
print ('Minute:' + str(today.minute))
print ('Second:' + str(today.second))


print ()

# This is an example asking for your birthday, and receiving the date as a string
# and converting it to a datetime object

birthday = input ('When is your birthday (mm/dd/yyyy)? ')
birthday_date = datetime.strptime(birthday, '%m/%d/%Y')
print ('Birthday: ' + str(birthday_date))

# Displaying the day before birthday just for fun
day_before = timedelta (days=1)
birthday_eve = birthday_date - day_before
print ('The day before your birthday was: ' + str(birthday_eve))
