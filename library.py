class Book:
    def __init__(self, title, author, isbn, genre):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.available = True


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        if book.isbn in self.books:
            print("Book already exists!")
        else:
            self.books[book.isbn] = book
            print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("Library is empty!")
            return

        for book in self.books.values():
            print(book.isbn, "-", book.title, "-", book.author)

    def search_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            print("Found:", book.title, "-", book.author)
        else:
            print("Book not found!")


library = Library()

# Book examples
library.add_book(Book("Python Basics", "John Smith", "101", "Programming"))
library.add_book(Book("Data Structures", "Jane Brown", "102", "Computing"))

# Show all books in system
print("\n--- All Books ---")
library.view_books()

# Search for a book
print("\n--- Search ---")
library.search_book("102")
