# Logical Operators - these are used to combine multiple conditinal statements
#           and - returns True if BOTH statements are true
#           or - returns True if one of the statements are true. 
#           not - reverses the result, False -> True, and True -> False

age = int(input("Enter your age | "))

temp = 20

sunny = False


if age >= 18 and age < 100:
    print("You are a valid user")
elif age < 18 and age > 0:
    print("You are too young to sign up")
else:
    print("You are not a valid age")


if temp <= 0 or temp >= 30:
    print("The temperature is bad")
else:
    print("The temperature is good")
    

if not sunny:
    print("It is not sunny")
else:
    print("It is sunny")