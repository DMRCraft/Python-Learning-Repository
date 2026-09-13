# Keyword arguments - an argument preceded by an identifier, helps with readability & order of arguments don't matter

# NOTE: If you are mixing positional and keyword arguments, POSITIONAL MUST BE FIRST!
# hello("Hello", title="Mr.", last="Ryan", first="Dylan")
# hello(title="Mr.", last="Ryan", first="Dylan", "Hello") ❌

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", "Mr.", "Dylan", "Ryan") # works as intended
hello("Mr.", "Hello", "Ryan", "Dylan") # techically works, but the order is wrong

hello(title="Mr.", greeting="Hello", last="Ryan", first="Dylan") # now it works properly

for x in range(1, 11):
    print("1", "2", "3", "4", sep="-") # end is a keyword argument, same with sep!



