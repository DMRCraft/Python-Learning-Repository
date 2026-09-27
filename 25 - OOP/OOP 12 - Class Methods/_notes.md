# Class Methods

Class methods allows operations related to the class itself.
They take (cls) as its first parameter, representing the class itself

- cls refers to the class that called method

```python
class Player:
    player_count = 0

    def __init__(self, name):
        self.name = name
        Player.player_count += 1

    @classmethod
    def get_player_count(cls):
        return cls.player_count


player1 = Player("Alex")
player2 = Player("Bob")

print(Player.get_player_count()) # -> 2
```

Above is a relatively basic example. You realistically could just use Player.player_count and still get the same value.
Here is an example where class methods become useful

```python
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    @classmethod
    def create_admin(cls, username):
        return cls(username, "admin")

admin = User.create_admin("Dylan")
```

This creates an admin User, without having to write User("Dylan", "admin") -> you don't need to remember the order of every attribute

Here is one more example I found online: (I edited a bit)

```python
class User:
    def __init__(self, username, age):
        self.username = username
        self.age = age

    @classmethod
    def from_string(cls, data):
        username, age = data.split(",")
        return cls(username, int(age))


user = User.from_string("Dylan,15")
print(user.name + ", " + user.age)
```

This is called an alternative constructor
