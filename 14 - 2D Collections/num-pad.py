# Num pad example
# Tuples are chosen since they are faster than lists + we dont need to change the values
# Sets NOT used since we need them ordered

num_pad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()