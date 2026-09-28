# Exception -> An event that interrupts the flow of a program
#              (ZeroDivisionError, TypeError, ValueError, etc)
# Look online to find a full list of errors!


#   try:
#   except Exception:
#   finally

try:
    number = int(input("Enter a number | "))
    print(1 / number)

except ZeroDivisionError:
    print("You can't divide by zero!!!")
except ValueError:
    print("You must only enter numbers")
except Exception:
    print("Something went wrong!")

finally:
    print("...Clean-up...")