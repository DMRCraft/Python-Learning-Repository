# Scope

**Variable scope** - where a variable is visible and accessible
**Scope resolution** - (LEGB) Local -> Enclosed -> Global -> Built-in

- Note that Local has the highest priority, enclosed next, etc

```python
def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

# A is LOCAL to func1. func2 cannot access it without accessing func1
```

```python
def func1():
    x = 1
    print(x)

def func2():
    x = 2
    print(x)

# We can make two different versions of the same variable name, since they have different scopes
```

```python
def func1():
    x = 1
    print(x)

    def func2():
        x = 2
        print(x)

    func2()
    print(x)

func1()

# Here is an advanced topic. To simplify it, in func2, we use its local variable
# in the main func1, x is one. func2 DOES NOT REASSIGN IT
# test it out in scope.py
```

```python
def func1():
    print(x)

def func2():
    print(x)

x = 1

# func1 + 2 will both use the global scope, since there are no local variables called x
```

```python


```
