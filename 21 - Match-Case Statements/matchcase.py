# Match-case statements (switch in other languages) -> an alternative to using an unecessary amount of "elif" statements
#   they execute some code IF a value matches a "case".
#   they are cleaner and the syntax is more readable


# NOTE: "|" means OR
def day_of_week(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            print("It is a weekday")
        case "Saturday" | "Sunday":
            print("It is the weekend")
        case _:
            print(f"{day} is not a valid day!")

day_of_week("Saturday")

def is_weekend(day):
        match day:
            case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                return False
            case "Saturday" | "Sunday":
                return True
            case _:
                return False

print(is_weekend("Monday"))