# LEGB -> local - enclosed - global - built-in
# (local has the highest priority, etc)

def func1():
    x = 1
    print(x)

    def func2():
        x = 2
        print(x)
    func2()

    print(x)

func1()

from math import e

def print_e():
    print(e)

e = 3
print_e()