# Minecraft-like inventory system

# Biggest lesson: None is a value, NOT A STRING

# There are a few things i *could* fix, but leaving since this was a quick project
#   for example, i could make a reusable function for the repeated printing commands: print_command(message)

import time

inventory = {}


def add_item():
    print()
    print("-- Add an item to your inventory --")

    item = ""
    while item == "":
        item = input("Name the item you want to add | ").lower()

    amount = 0
    while amount <= 0:
        amount = int(input(f"Enter the amount of '{item}'s you want to add | "))

    item_count = inventory.get(item)

    if item_count is None:
        inventory.update({item.lower(): amount})
    else:
        inventory.update({item.lower(): item_count + amount})

    print(f"Successfully added {amount} '{item}'(s) to your inventory!")


def remove_item():
    print()
    print("-- Remove an item from your inventory --")
    
    item = ""
    while item == "":
        item = input("Name the item you want to remove | ").lower()

    if item in inventory:
        inventory.pop(item)
        print(f"Successfully removed all of your '{item}'s")
    

def inspect_inventory():
    print()
    print("-- Inspecting Inventory --")
    print(f"Here is your current inventory (you have {len(inventory)} unique items)")

    for key, value in inventory.items():
        print(f"{key}: {value}")


def search_inventory():
    print()
    print("-- Search Inventory --")
    item = ""
    while item == "":
        item = input("Enter the item you want to find | ").lower()

    item_count = inventory.get(item)
    if item_count == None:
        print(f"You do not have any '{item}'s")
    else:
        print(f"You have {item_count} '{item}'s")


while True:
    print("----------")
    print("Add item: 'a'")
    print("Remove item: 'r'")
    print("View your inventory: 'e'")
    print("Search your inventory: 's'")
    print("Quit: 'q'")
    print("----------")

    print()
    
    response = input("What would you like to do? ")

    if response.lower() == "a":
        add_item()
    elif response.lower() == "r":
        remove_item()
    elif response.lower() == "e":
        inspect_inventory()
    elif response.lower() == "s":
        search_inventory()
    elif response.lower() == "q":
        break

    time.sleep(0.25)

print("Closing program, thanks for using!")
