# Decorators

A decorator is a function that takes another function and **extends / modifies** its behavior without changing the original function's code

## Basic Syntax

```python
def decorator(func):
    def wrapper():
        # Extra behavior
        func() # -> call the function
        # More extra behavior

    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
```

- @decorator is basically shorthand to: `say_hello = decorator(say_hello)

## Why use decorators?

They are useful when you want to add the same behavior to multiple functions
Here is an example I found -> A useful "timer" function

```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()

        print(f"Took {end - start:.2f} seconds")

    return wrapper


@timer
def task():
    print("Doing something...")

task()
```

- @timer can be reused for as many functions as you want!

## Use cases:

Authentication -> Checks whether someone is logged in
Permissions -> Checks whether someone is allowed to perform an action
Logging -> Records when/functions are called
Timing -> Measures how long functions take
Caching -> Stores previous results

## Decorators with arguments

A decorator's wrapper needs \*args and \*\*kwargs so it can work with functions with different parameters

- Take all arguments, and pass them back to the function

```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the add function")
        result = func(*args, **kwargs) # add() returns the value here, since it is called here.
        print("After the add function")

        return result # <- returns from wrapper()

    return wrapper # <- returns from decorator()

@decorator
def add(a, b):
    print("Doing the main add function")
    return a + b

print(add(1, 2))

# Output:
#   Before the add function
#   Doing the main add function
#   After the add function
#   3
```

Think of it as:
@decorator -> decorator(add) -> creates the wrapper function -> returns it to @decorator -> add is now wrapper

The add function is now:

```python
def add(a, b):
    print("Before the add function")
    print("Doing the main add function")
    print("After the add function")
    return a + b
```
