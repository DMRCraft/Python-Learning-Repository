import math

# find the hypotneuse of a triangle using user input
# the formula is: c = sqrt(a^2 + b^2)

a = float(input("Enter side A | "))
b = float(input("Enter side B | "))

c = math.sqrt(a**2 + b**2) # could also use math.pow, but my answer is shorter and easier to read


print(f"The hypotneuse is {c}")