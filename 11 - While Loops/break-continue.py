# Break - immediately terminates the inntermost loop
# Continue - skips the remaining statements in the current iteration and continues to the next iteration of that loop

count = 0

while True:
    count += 1
    if count % 2 == 0:
        continue
    print(count)

    if count >= 20:
        break



