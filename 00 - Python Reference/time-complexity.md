# Time complexity

Time complexity is a theoretical measure of how the running time of a piece of code / algorithm grows as the size of its input (n) increases
We use Big O notation

### Constant time O(1) (The execution time stays identical no matter how large the input data gets)

```python
x = 10
y = x + 5
```

### Linear Time O(n) (The running time scales in direct proportion to the input size)

```python
for item in items:
    print(item)
```

### Quadratic Time O(n^2) (The time grows proportionally to the square of the input size, usually seen in nested loops)

```python
for item in items:
    for other in items:
        print(item, other)
```

### Nested loops with different sizes O(nm)

```python
for item in items:
    for value in values:
        print(item, value)
```
