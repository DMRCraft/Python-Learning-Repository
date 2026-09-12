# Conditional Expression - one-line shortcut for the if-else statement, called a ternary operator
#                       print / assign one of two values based on a conditon
#                       X if condition else Y

num = 5

a = 6
b = 7

user_role = "admin"

print("Positive" if num >= 0 else "Negative")
result = "Even" if num % 2 == 0 else "Odd"

max_num = a if a > b else b
min_num = a if a < b else b

access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)