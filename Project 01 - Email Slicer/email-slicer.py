# NOTE: if the user's answer does NOT include a "@", the program breaks
# this is because ".index" is used when we are sure the value in the string 100% exists

email = input("Enter your email | ")

at_index = email.index("@")

username = email[0:at_index] # start at index 0, and end right before reaching "@"
domain = email[at_index + 1:] # start right after the "@", and continue to the end

print(f"Username: {username} | Domain: {domain}")