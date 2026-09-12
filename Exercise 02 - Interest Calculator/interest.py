# Compound interest calculator
# Checks each, and doesnt allow values below 0

principle = 0
rate = 0
time = 0

amount = 0

while principle <= 0:
    principle = float(input("Enter the principle amount | "))
    if principle <= 0:
        print("The principle must be above zero")

while rate <= 0:
    rate = float(input("Enter the interest rate | "))
    if rate <= 0:
        print("The interest rate must be above zero")

while time <= 0:
    time = float(input("Enter the time in years | "))
    if time <= 0:
        print("The time must be above zero")

amount = principle * pow((1 + rate / 100), time)
print(amount)

        