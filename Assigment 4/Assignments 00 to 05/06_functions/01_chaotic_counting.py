import random

DONE_LIKELIHOOD = 0.3  # You can adjust this value to make it more or less likely to stop early

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Exit the function early if done() returns True
        print(curr_num)

def done():
    """Returns True with a probability defined by DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

# Required to run the program
if __name__ == '__main__':
    main()
