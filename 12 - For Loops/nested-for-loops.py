# Nested loop - a loop within another loop (outer, inner)



while True:
    rows = int(input("Enter the rows | "))
    cols = int(input("Enter the columns | "))
    symbol = input("Enter a symbol | ")

    for x in range(rows):
        for y in range(cols):
            print(symbol, end="")
        print()