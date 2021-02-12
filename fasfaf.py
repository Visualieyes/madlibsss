

failed_guesses = 0
numGuesses = 6
s = ''
word = 'racecar'


correct_letters_guessed = []
failed_letters_guessed = []

while failed_guesses < numGuesses:
    guess = input("Guess a letter: ")
    failed_guesses += 1
    
    if guess in word:
        correct_letters_guessed.append(guess)
        print("Correct ")
        print("String: ", correct_letters_guessed)
        print("Letters guessed ", failed_letters_guessed)
    elif guess not in word:
        failed_letters_guessed.append(guess)
        print("Incorrect")
        print("String: ", correct_letters_guessed)
        print("Letters guessed: ", failed_letters_guessed)
        
        
        
        
