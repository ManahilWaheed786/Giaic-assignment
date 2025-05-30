class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


# Example usage
if __name__ == "__main__":
    book1 = Book("The Alchemist")
    book2 = Book("1984")
    book3 = Book("To Kill a Mockingbird")

    print(f"Total Books: {Book.total_books}")
