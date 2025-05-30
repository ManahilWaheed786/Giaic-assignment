import random
import string

def get_random_word():
    word_list = ['python', 'hangman', 'programming', 'challenge', 'computer', 'random']
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    displayed = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(displayed)

def main():
    print("Welcome to Hangman!")
    word = get_random_word()
    guessed_letters = set()
    attempts_left = 6  # Number of allowed wrong guesses

    while attempts_left > 0:
        print("\nWord to guess:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts_left}")
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").upper()

        # Validate input
        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("Please enter a single letter (A-Z).")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            # Check if all letters guessed
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts_left -= 1

    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    main()
