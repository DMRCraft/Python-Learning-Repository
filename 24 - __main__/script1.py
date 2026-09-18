# print(f"This is script1: {__name__}") # prints "main" if you run the file directly

print(f"This is script1: {__name__}")

# from script2 import *

def fav_food(food):
    print(f"Your favourite food is {food}")

def main():
    print("This is script1's main")
    fav_food("Pizza")
    print("Goodbye")

if __name__ == "__main__":
    main()