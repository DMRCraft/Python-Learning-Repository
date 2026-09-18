from script1 import *

def fav_drink(drink):
    print(f"Your favourite drink is {drink}")

print(f"This is script2: {__name__}")

def main():
    print(f"This is script2's main")

    fav_food("Sushi")
    fav_drink("Cola")

    print("Goodbye!")


if __name__ == "__main__":
    main()
