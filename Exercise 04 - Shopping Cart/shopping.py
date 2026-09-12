# Shopping cart program

# some notes:
# lists used since we need to add values, and I personally wanted them ordered

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price for the {food}: €"))
        foods.append(food)
        prices.append(price)

print("--- Cart ---")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print("----------")
print(f"Your total is €{total}")