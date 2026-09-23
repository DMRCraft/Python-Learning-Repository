# Class attributes

A class attribute is an attribute defined directly inside a class, which is shared by instances of that class.
An instance can provide its own value for the class attribute by changing it to an instance attribute

```python
class User:
    online = True

    def __init__(self, name):
        self.name = name

user1 = Player("Dylan")
user2 = Player("John")

user1.online = False # -> this creates an instance attribute. This does not affect the class attribute

# ---

User.online # -> access the class attribute using the class itself
User.online = False # -> changes the class attribute

```

## Class attribute VS Instance attribute

Use:

- **Class attributes** for information shared by the class.
- **Instance attributes** for information specific to each object.
