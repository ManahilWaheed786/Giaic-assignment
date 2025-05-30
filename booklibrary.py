import json
import os

LIBRARY_FILE = 'library.json'

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, 'r') as file:
            return json.load(file)
    return []

def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    try:
        year = int(input("Enter publication year: "))
    except ValueError:
        print("Invalid year. Book not added.")
        return
    genre = input("Enter genre: ").strip()
    read_input = input("Have you read this book? (y/n): ").strip().lower()
    read = read_input == 'y'
    
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    removed = False
    for book in library:
        if book['title'].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed.")
            removed = True
            break
    if not removed:
        print(f"No book found with title '{title}'.")

def search_books(library):
    keyword = input("Enter title or author to search: ").strip().lower()
    found_books = [book for book in library if keyword in book['title'].lower() or keyword in book['author'].lower()]
    if found_books:
        print("\nFound Books:")
        for book in found_books:
            print_book(book)
    else:
        print("No matching books found.")

def display_books(library):
    if not library:
        print("Library is empty.")
        return
    print("\nAll Books:")
    for book in library:
        print_book(book)

def print_book(book):
    read_status = "Read" if book['read'] else "Unread"
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {read_status}")

def display_statistics(library):
    total = len(library)
    if total == 0:
        print("Library is empty.")
        return
    read_count = sum(book['read'] for book in library)
    percent_read = (read_count / total) * 100
    print(f"Total books: {total}")
    print(f"Books read: {read_count} ({percent_read:.2f}%)")

def main():
    library = load_library()
    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_books(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            save_library(library)
            print("Library saved. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 6.")

if __name__ == "__main__":
    main()
