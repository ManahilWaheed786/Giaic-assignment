import random

NUM_ROUNDS = 5  # You can change this number to play more rounds

def get_user_guess():
    """Prompt user to input 'higher' or 'lower'. Repeat until valid input."""
    while True:
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if guess in ("higher", "lower"):
            return guess
        print("Please enter either higher or lower:")

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")

        user_num = random.randint(1, 100)
        comp_num = random.randint(1, 100)

        print(f"Your number is {user_num}")
        user_guess = get_user_guess()

        # Determine if user guess is correct
        if user_num == comp_num:
            # If numbers are equal, computer wins (user loses)
            correct = False
        elif user_guess == "higher" and user_num > comp_num:
            correct = True
        elif user_guess == "lower" and user_num < comp_num:
            correct = True
        else:
            correct = False

        if correct:
            score += 1
            print(f"You were right! The computer's number was {comp_num}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")

        print(f"Your score is now {score}\n")

    print("Thanks for playing!")

    # Conditional ending messages based on score
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
