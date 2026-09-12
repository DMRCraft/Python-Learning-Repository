
price1 = 31230.1415
price2 = -981.65
price3 = 12.34

print(f"Price 1: €{price1:.2f}") 
print(f"Price 2: €{price2:.2f}") # adds / removes decimal portions to have 2 nums
print(f"Price 3: €{price3:.2f}") 

print("-----")

print(f"Price 1: €{price1:10}") 
print(f"Price 2: €{price2:10}") # adds / removes decimal portions to have 2 nums
print(f"Price 3: €{price3:10}") 

print("-----")

print(f"Price 1: €{price1:010}") 
print(f"Price 2: €{price2:010}") # adds / removes decimal portions to have 2 nums, and 0 pads them
print(f"Price 3: €{price3:010}") 

print("-----")

print(f"Price 1: €{price1:<10}") 
print(f"Price 2: €{price2:<10}") # left justifies them
print(f"Price 3: €{price3:<10}") 

print("-----")

print(f"Price 1: €{price1:>10}") 
print(f"Price 2: €{price2:>10}") # right justifies them
print(f"Price 3: €{price3:>10}") 

print("-----")

print(f"Price 1: €{price1:^10}") 
print(f"Price 2: €{price2:^10}") # center justifies them
print(f"Price 3: €{price3:^10}") 

print("-----")

print(f"Price 1: €{price1:+}") 
print(f"Price 2: €{price2:+}") # if a number is positive, adds a "+" symbol to the start
print(f"Price 3: €{price3:+}") 

print("-----")

print(f"Price 1: €{price1: }") 
print(f"Price 2: €{price2: }") # if a number is positive, adds a space to the start
print(f"Price 3: €{price3: }") 

print("-----")

print(f"Price 1: €{price1:,}") 
print(f"Price 2: €{price2:,}") # thousand seperator
print(f"Price 3: €{price3:,}") 

print("-----")

print(f"Price 1: €{price1:%}") 
print(f"Price 2: €{price2:%}") # adds a precentage to each
print(f"Price 3: €{price3:%}") 


# We can combine multiple flags

print("-----")

print(f"Price 1: €{price1:+,.2f}") 
print(f"Price 2: €{price2:+,.2f}") # thousand seperator
print(f"Price 3: €{price3:+,.2f}") 