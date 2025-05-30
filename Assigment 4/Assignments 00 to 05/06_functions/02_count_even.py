def count_even(lst):
    """
    Returns and prints the number of even numbers in the given list.
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    print(count)

def get_list_of_ints():
    """
    Prompts the user to enter integers until they press Enter.
    Returns the list of entered integers.
    """
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")
    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

# Required entry point for the program
if __name__ == '__main__':
    main()
