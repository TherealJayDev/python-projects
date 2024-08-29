import random

words = ['python', 'hangman', 'challenge', 'programming', 'developer']
max_guesses = 6

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("Welcome to Hangman!")

    while wrong_guesses < max_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) <= guessed_letters:
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {max_guesses - wrong_guesses} guesses left.")
        
        if wrong_guesses == max_guesses:
            print(f"\nGame Over! The word was: {word}")
            break

    if input("Play again? (y/n): ").lower() == 'y':
        hangman()

if __name__ == "__main__":
    hangman()
