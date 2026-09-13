import random

# print(dir(random))

number = random.randint(1, 6) # random integer between 1 - 6, like a dice

low = 1
high = 100

number = random.randint(low, high) # random integer between 1 - 6, like a dice
float_num = random.random() # random float between 0.0 and 1.0

options = ("rock", "paper", "scissors")
choice = random.choice(options)


cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
random.shuffle(cards)

print(cards)