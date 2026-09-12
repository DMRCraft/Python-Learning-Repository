# Collections (will add to as I discover note-worthy points)

## What is the point of tuples, if you can't change or add to them?

Simply, they are used for a grouped set of values that are guarenteed to not be changed <br>
E.g: cords = (10, 20) <br>
Another example: location = {
(10, 20): "Home",
(100, -20): "Village"
}

## enumerate()

Use for cases like this:

```python
foods = ["apple", "carrot", "pizza"]

for iteration_num, food in enumerate(foods, start=1):
    print(f"{iteration_num}: {food}")

# output: 1: apple  2: carrot  3: pizza

```

- enumerate turns: foods = ["apple", "carrot", "pizza"]
- into pairs: (0, "apple") (1, "banana") (2, "pizza")
