def main():
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words:")

    # Get inputs from user
    adjective = input("Adjective: ")
    noun = input("Noun: ")
    verb = input("Verb (past tense): ")
    place = input("Place: ")
    food = input("Food: ")

    # Create the story using f-string
    story = f"""
    Today I went to the {place}. It was a very {adjective} day.
    I saw a {noun} that {verb} right in front of me!
    After that, I was so hungry I ate some {food}.
    What a day!
    """

    # Print the story
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
