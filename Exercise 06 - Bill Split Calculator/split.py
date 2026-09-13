# Smart Tip & Split Calculator
# Skills used: user input, math, time module, format specifiers and functions

import time

print("----- Smart Tip & Split Calculator -----")

def tip_calculator():
    print("----------")

    bill_total = float(input("Enter the bill total | "))
    tip_prec = float(input("Enter the tip as a decimal precentage | "))
    num_of_people = int(input("Enter the amount of people | "))

    total_tip = bill_total * tip_prec

    total_cost = bill_total + total_tip
    split_bill = total_cost / num_of_people

    print("----------")
    print(f"Your bill including a €{total_tip:.2f} tip is €{total_cost:.2f}")
    print(f"With {num_of_people} at the table, each person has a bill of €{split_bill:.2f}")
    print("----------")

while True:
    using = input("Type 'u' to use, or 'q' to quit | ")

    if using.lower() == "u": tip_calculator()
    elif using.lower() == "q": break
    time.sleep(1)

print("Quitting, see you later!")

# Had an issue with the restarting not working properly. I was able to fix it and clean up unecessary loops
# My original solution was:
# while True:
#     tip_calculator()

#     restarting = ""
#     while restarting.lower() != "r":
#         restarting = input("Type 'r' to restart, or 'q' to quit | ")
#         if restarting.lower() == "q":
#             break



