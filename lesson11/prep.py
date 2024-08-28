# This lesson will go over opening & reading files in Python

# open the file name
#if you use the with function you do not need this line of code!
#games_file = open ("lesson11/games.txt")

# be sure to close the file when you are done
with open ("lesson11/games.txt") as games_file:
    # For loop to display all the items in the txt file
    for line in games_file:
        print (line)


sentence = "I will go and do"

words = sentence.split(" ")
# The variable "words" is now a list that contains each word.

# You can iterate through each word and do something with it, such as display it:
for word in words:
    print(word)
# You can also add things like commas between words in the split function
# that will display something like this
# I,
# will,
# go,