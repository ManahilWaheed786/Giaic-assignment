import random

NUM_SIDES = 6

def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    print(f"Die 1: {die1}, Die 2: {die2}")

def main():
    roll_dice()
    roll_dice()
    roll_dice()

if __name__ == '__main__':
    main()
