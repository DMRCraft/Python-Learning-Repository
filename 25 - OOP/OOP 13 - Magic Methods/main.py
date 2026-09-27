# Magic methods -> Commonly also known as "dunder methods".
#                  They are automatically called by many of Python's built-in operations.
#                  They allow developers to define / customize the behavior of objects
#                  Some examples: __init__, __str__, __eq__


class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"
    

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages
    

    def __add__(self, other):
        return self.num_pages + other.num_pages
    

    def __contains__(self, keyword):
        return keyword in self.title  or   keyword in self.author


    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found!"


# __init__ is automatically called when instantiating an object
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Harry Potter", "J.K. Rowling", 223)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

book4 = Book("The Hobbit", "J.R.R. Tolkien", 999)

print("-----")

# __str__ is called when you convert an object to a string with str()
# This includes an f string, printing, directly using str(), etc
#   For context, print() basically does print(str(object))
print(book1)
print(book2)
print(book3)

# __eq__ is called when the equality operator (==) is used to compare an object with another value.
print(book1 == book4) # Without __eq__, it compares memory addresses


# __lt__ and __gt__ are called when the comparative operators are used to compare an object with another value
print(book2 < book3) # Without __lt__, it throws a TypeError, since Python doesn't know what to compare
print(book2 > book3) # ^


# __add__ is called when the + operator is used with an object as the left operand.
print(book1 + book2)


# __contains__ is called when the membership operator "in" is used
print("Lion" in book3)
print("Rowling" in book2)


# __getitem__ is called when the index operator [] is used
print(book1["title"])
print(book2["author"])
print(book3["pages"])
print(book4["movie"])

