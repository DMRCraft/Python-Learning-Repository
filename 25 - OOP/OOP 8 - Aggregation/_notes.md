# Aggregation

Aggregation is an OOP relationship where one object (the whole) contains **_references_** to one or more INDEPENDENT objects (the parts)  
Think of it as a **"has-a"** relationship

One object stores references to other objects, often with collections. Note REFERENCES, since the objects can still behave and exist independently .

An analogy is **"I have/group you, but you _can_ exist without me"**

```python
class Library:
    def __init__(self, books):
        self.books = books


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Harry Potter", "J.K Rowling")
book2 = Book("Lord of the Rings", "J. R. R. Tolkien")
book3 = Book("The Hunger Games", "Suzanne Collins")

library = Library([book1, book2, book3])

for book in library.books:
    print(book.title + ": " + book.author)

```

- The `Book` objects are created separately from the `Library`.
- A `Book` can exist without being inside a `Library`.
- The `Library` groups/uses the `Book` objects.
- The contained objects are not dependent on the container
