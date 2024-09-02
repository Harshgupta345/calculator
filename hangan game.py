import random
import string
lowercase=string.ascii_lowercase
def choose_word():

    return random.choices(lowercase,k=4)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts remaining: {attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Incorrect guess.")
        
        if attempts == 0:
            print(f"Game over! The word was: {word}")

# Run the game
hangman()