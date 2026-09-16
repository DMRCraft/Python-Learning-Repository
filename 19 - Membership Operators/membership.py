# Membership operators - used tp test whether a value or variable is found in a sequence
#   e.g: string, list, tuple, set, dictionary, etc

# in  /  not in -> returns a Boolean value

word = "APPLE"
letter = "A" # True
letter = "a" # False, must be identical


if letter in word: print(f"{letter} is in {word}")
else: print(f"{letter} not found")

if letter not in word: print(f"{letter} not found")
else: print(f"{letter} is in {word}")

# ---

students = {"John", "Jack", "Jill"}
student = "John"
if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} is not a student")