# Aggregation is an OOP relationship where one object   (the whole)
#             contains references to one or more INDEPENDENT objects (the parts)
#             think of it as a "has-a" relationship

# "I have/group you, but you can exist without me"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [f"{book.title} by {book.author}" for book in self.books]


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


library = Library("Central Library")

book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("Lord of the Rings", "J. R. R. Tolkien")
book3 = Book("The Hunger Games", "Suzanne Collins")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

print(library.name)

for num, book in enumerate(library.list_books(), start=1):
    print(f"{num}. {book}")
