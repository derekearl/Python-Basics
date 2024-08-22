# Prove assignment for CSE 110 creating a game based off of wordle


# Set the word

word = 'apple'

# Display a welcome to the user
print ('Welcme to the Guessing game. Based off on Wordle')
print ()


print ('Try to guess a five letter word ')
# Display the hint with underscores (_)

for i in range(len(word)):
    print ('_ ', end='')
    
print ()


guess = ''
attempts = 0

while guess != word:
    hint = ''
    attempts += 1
    # Ask for a guess
    guess = input ('What is your guess? ')

    # If the guess is correct, then give them a congrats
    if guess == word:
        print (f"Congrats you guessed the word '{word}' in {attempts} attempts! ")

    # If the guess is not equal to the number of letters from the hint, give a error message
    elif len(guess) != len(word):
        print ('Sorry the number of letters must match the number of underscores')
        guess = input ('What is your guess? ')

    # Oterwise display a hint
    else:
        print ('Try Again! ')
        
        for i in range(len(word)):
            print ('_ ', end='')
        
    print ()

    for i in range(len(word)):
        if guess[i] == word[i]:
            hint += guess[i].upper()
        elif guess[i] in word:
            hint += guess[i].lower()
    else:
            print(f"Hint: {hint}")

print ('Try changing the word and play again!')