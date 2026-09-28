# Recursion -> a function that calls itself from within
#              Helps to visualize a complex problem into basic steps,
#              which can be solved more easily iteratively /  recursively

# iterative -> faster but more complex
# recursive -> slower but simpler

# --- ITERATIVE ---

def walk(steps):
    for step in range(1, steps + 1):
        print(f"You take step #{step}")

# walk(100)


# --- RECURSIVE ---

def walk_2(steps):
    if steps == 0:
        return
    walk_2(steps - 1)
    print(f"You take step #{steps}")

walk_2(100)

# steps = 100 -> steps - 1 (99) -> 98 ... steps == 0, return

