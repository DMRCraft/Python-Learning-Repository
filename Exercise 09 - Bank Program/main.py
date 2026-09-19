# Bank program
# Topics / skills used:

# Functions,
# Collections (lists, tuples)
# enumerate
# User input + basic validation (error handling isn't added)
# Unpacking -> basic usage, I will learn properly later (did get help with that part)
# __name__ == "__main__" + main function
# basic logic + math

# Had a lot of fun working on this! There are some places to improve, but nothing much
# The biggest would be error handling and editing the original balance to save the formatting

# Deposits money into the account and returns the updated balance.
def deposit_money(balance, history):
    amount = 0
    while amount <= 0:
        amount = float(input("How much do you request to deposit? | "))

    amount = round(amount, 2)
    balance += amount
    history.append(("Deposit", amount, balance))

    print(f"Your new balance is: {balance:.2f}")

    return balance

# Withdraws money only if the balance is left >= 0
def withdraw_money(balance, history):
    amount = 0
    while amount <= 0:
        amount = float(input("How much do you request to withdraw? | "))

    amount = round(amount, 2)

    if balance - amount < 0:
        print("You cannot withdraw more than you have!")
    else:
        balance -= amount
        history.append(("Withdrawal", amount, balance))
        print(f"Your new balance is: {balance:.2f}")

    return balance


def check_balance(balance):
    print("----------")
    print(f"Your current balance is: €{balance:.2f}")
    print()

def view_history(history):
    for num, item in enumerate(history, start=1): # enumerate() provides a number alongside each transaction
        type, amount, balance = item # unpacks item
        print(f"{num}) Type: {type} | Amount: €{amount:.2f} | Balance: €{balance:.2f}")

def main():
    balance = 500
    transaction_history = []
    

    print("----- Bank -----")

    while True:
        response = input("What would you like to do? | ")
        match response.lower():
            case "d": balance = deposit_money(balance, transaction_history)
            case "w": balance = withdraw_money(balance, transaction_history)
            case "b": check_balance(balance)
            case "v": view_history(transaction_history)
            case "q": break

    print("Closing")

if __name__ == "__main__":
    main()

