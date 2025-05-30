def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range."

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Element at index {index} updated."
    else:
        return "Index out of range."

def slice_list(lst, start, end):
    # Clamp indices to valid ranges
    start = max(0, start)
    end = min(len(lst), end)
    if start >= end:
        return []
    return lst[start:end]

def main():
    # Initialize the list
    elements = ['apple', 42, 'banana', 3.14, 'orange']

    print("Welcome to the Index Game!")
    print("Current list:", elements)

    while True:
        print("\nChoose an operation:")
        print("1 - Access element")
        print("2 - Modify element")
        print("3 - Slice list")
        print("4 - Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            idx = input("Enter the index to access: ").strip()
            if not idx.isdigit():
                print("Please enter a valid non-negative integer index.")
                continue
            idx = int(idx)
            result = access_element(elements, idx)
            print(f"Result: {result}")

        elif choice == '2':
            idx = input("Enter the index to modify: ").strip()
            if not idx.isdigit():
                print("Please enter a valid non-negative integer index.")
                continue
            idx = int(idx)
            new_val = input("Enter the new value: ")
            # Try to interpret numbers automatically
            if new_val.isdigit():
                new_val = int(new_val)
            else:
                try:
                    new_val = float(new_val)
                except ValueError:
                    pass  # keep as string
            result = modify_element(elements, idx, new_val)
            print(result)
            print("Updated list:", elements)

        elif choice == '3':
            start = input("Enter start index: ").strip()
            end = input("Enter end index (exclusive): ").strip()
            if not (start.isdigit() and end.isdigit()):
                print("Please enter valid non-negative integer indices.")
                continue
            start, end = int(start), int(end)
            sliced = slice_list(elements, start, end)
            print(f"Sliced list: {sliced}")

        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
