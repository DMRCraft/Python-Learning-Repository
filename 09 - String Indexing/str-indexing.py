# indexing - accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

# NOTE: the ending is exclusive

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # logs the first index (which is 1)


print(credit_number[0 : 4]) # logs the first 4 index. 
print(credit_number[:4]) # same as above, 0 *can* be left out, better to keep it in for readability
print(credit_number[5:9])
print(credit_number[5:]) # if you want X -> the last digit, you do not need the ending number (the colon IS needed however)

print(credit_number[-1]) # logs the LAST digit. Negative numbers start from the end (right -> left)


print(credit_number[::]) # logs start to end
print(credit_number[::2]) # logs every second character from start to end
print(credit_number[::3]) # logs every third character from start to end





