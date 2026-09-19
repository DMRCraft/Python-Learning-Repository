# Arguments, References & Mutability

## Core idea

Python variables are **names that refer to objects**.
When an object is passed to a function, the function receives a reference to the **same object**.

```python
items = [1, 2, 3]

def add_item(items):
    items.append(4)

add_item(items)

print(items)  # [1, 2, 3, 4]
```

`items` inside and outside the function refer to the same list.

## Mutable vs Immutable

### Mutable objects

Can be changed in place:

- `list`
- `dict`
- `set`

Changes made inside a function affect the original object.

```python
def add_item(items):
    items.append(4)
```

### Immutable objects

Cannot be changed in place:

- `int`
- `float`
- `str`
- `tuple`
- `bool`

If a function creates a new value, return it and assign it:

```python
balance = deposit_money(balance)
```

```python
def deposit_money(balance):
    balance += 100
    return balance
```

## Can a function change the original variable?

**Not by simply reassigning its parameter.**

```python
x = 10

def change(x):
    x = 20

change(x)

print(x)  # 10
```

The function's `x` is a local name. Reassigning it does not change the caller's `x`.

However, if the argument refers to a mutable object, the object itself can be modified:

```python
numbers = [1, 2, 3]

def change(numbers):
    numbers.append(4)

change(numbers)

print(numbers)  # [1, 2, 3, 4]
```

## Rule of thumb

**Mutable object → modify it directly**

```python
my_list.append(value)
```

**Immutable value → return the new value**

```python
x = function(x)
```

## Important terminology

Python is commonly described as using **pass-by-assignment** (or **pass-by-object-reference**).

The important mental model is:

> The function receives a reference to the same object, but its parameter is a separate local name.
