# Prove assignment for the Mad Libs activity

print ('Welcome to the Mad Libs activity, please enter the following prompts')
print ()

plural_noun = input ('Please enter a plural noun: ')
adjective = input ('Please enter an adjective: ')
verb_1 = input ('Please enter a verb: ')
noun_1 = input ('Please enter a noun: ')
exclamation = input ('Please enter an exclamation:  ')
verb_2 = input ('Please enter another verb:  ')
noun_2 = input ('Please enter another noun:  ')
print()

output = (f'So the other day there were these {plural_noun} that were in a {adjective} mood,\n'
    f'When one of them came up to me with a smile on their face, I could not help but {verb_1} in astonishment.\n'  
    f'When all of a sudden a {noun_1} came to see what was all the commotion about.  All of a sudden the {noun_1}\n'
    f'shouted {exclamation} and did a {verb_2} because of what he saw.  Then all of a sudden a {noun_2} appeared. ')


# Story will be displayed below
print('Here is your story:  ')
print(output)