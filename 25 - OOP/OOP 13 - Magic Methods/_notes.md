# Magic Methods

Magic methods, commonly also known as "dunder methods", are automatically called by many of Python's built-in operations.  
They allow developers to define / customize the behavior of objects.

## List of common methods:

| Name           | When it is called                                | Operation / Condition            |
| -------------- | ------------------------------------------------ | -------------------------------- |
| `__init__`     | When an object is initialized                    | Class(...)                       |
| `__str__`      | When an object is converted to a string          | str(obj) / print(obj) / f"{obj}" |
| `__eq__`       | When two objects are compared for **equality**   | obj1 == obj2                     |
| `__ne__`       | When two objects are compared for **inequality** | obj1 != obj2                     |
| `__len__`      | When the length of an object is requested        | len(obj)                         |
| `__contains__` | When membership is checked                       | value in obj                     |
| `__getitem__`  | When an item is accessed                         | obj(key)                         |

### Comparison methods

- `__lt__` | obj1 < obj2
- `__le__` | obj1 <= obj2

- `__gt__` | obj1 >= obj2
- `__ge__` | obj1 >= obj2

### Arithmetic / Math Operators

- `__add__` | obj1 + obj2
- `__sub__` | obj1 - obj2
- `__mul__` | obj1 \* obj2
- `__pow__` | obj1 \*\* obj2
- `__truediv__` | obj1 / obj2
- `__floordiv__` | obj1 // obj2
- `__abs__` | abs(obj)

## Note:

- In most binary operators, the object on the **left** is the one whose magic method is called
  For example, `a + b` becomes `a.__add__(b)`
