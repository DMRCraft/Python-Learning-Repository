# For loops - exectures ablock of code a FIXED number of times.
# You can iterate over a range, string, sequence, etc

# for (count_var) in range(start, end, step)

# NOTE: Look at time-complexity in Python reference to see what each example is

for x in range(1, 11): # "11" is exclusive, so not counted. Runs 1 - 10
    print(x)

for x in range(10): # logs 0 - 10
    print(x)

for x in reversed(range(1, 11)): # reverse order, 10 - 1
    print(x)

for x in range(1, 11, 2): # 1 - 10 in steps of two
    print(x)

for x in range(1, 21):
    if x == 13:
        continue
    if x == 15:
        break
    print(x)

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

