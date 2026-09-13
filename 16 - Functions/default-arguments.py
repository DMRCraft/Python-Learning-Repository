# default arguments - default value for certain parameters
#                     the default is only used IF that argument is omitted

# NOTE: you must keep default arguments at the end.
# def count(start=0, end) ❌
# def count(end, start=0) ✔️


def add(x, y):
    return x + y

# add(1) # TypeError, since the second argument is not given


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))           # works, since discount defaults to 0, and tax defaults to 0.05
print(net_price(500, 0.1))      # only the discount's default is changed, tax is still 0.05
print(net_price(500, 0.1, 0))   # you can still change the argument's values


import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("TIME OVER")

count(10) # start at 0, end at ten
count(20, 10) # but you can still change the default