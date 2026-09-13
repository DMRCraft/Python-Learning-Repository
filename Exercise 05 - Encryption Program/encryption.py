import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters # all a single string
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

# ENCRYPTION

plain_text = input("Enter a message to encrypt | ")
cipher_text = ""

# for every letter in plain_text, find the index in the "chars" list, and add the corresponding letter from the "key" list to cipher_text
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# DECRYPTION

cipher_text = input("Enter a message to decrypt | ")
plain_text = ""

# for every letter in cipher_text, find the index in the "key" list, and add the corresponding letter from the "chars" list to plain_text
for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Original message: {cipher_text}")
print(f"Decrypted message: {plain_text}")