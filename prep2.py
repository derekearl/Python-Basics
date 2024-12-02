# More prep on using user defined functions

from datetime import datetime

def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Derek'
print_time('First Name Entered')

for i in range(0,10):
    print(i)
    
print_time('Loop Completed')