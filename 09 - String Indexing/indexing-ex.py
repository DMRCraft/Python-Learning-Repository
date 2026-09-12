# Given a credit card, get the last four digits

credit_card = "1234-5678-9012-3456"

last_digits = credit_card[len(credit_card) - 4 :] # my original solution, works but lengthy

last_digits = credit_card[-4:] # the best solution. -4 means start from the 4th last digit, the : means count until the end from that start index

print(f"XXXX-XXXX-XXXX-{last_digits}")


# Given a string, reverse the characters

string = "DMRCraft"

reversed_string = string[::-1] # negative step, goes backwards

print(f"{string} => {reversed_string}")