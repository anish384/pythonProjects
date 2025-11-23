# aggregation - "has-a" 
class Library:
    def __init__(self, name):
        self.name = name
        self.books = [] # The Container: A list to hold external objects

    def add_book(self, book):
        # AGGREGATION HAPPENS HERE
        # We are passing an existing object (book) into the Library.
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# 1. INDEPENDENT EXISTENCE
# We create the books OUTSIDE the library.
# They exist whether the library exists or not.
book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("1984", "George Orwell")

# 2. THE ASSOCIATION
library = Library("New York Public Library")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for book_info in library.list_books():
    print(book_info)

# If we were to delete the library now:
del library
# The books would STILL exist in memory!
print(f"The library is gone, but {book1.title} is still here.")
