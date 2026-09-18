# Module - a file containing code you want to include in your program
#          use "import" to include a module
#          you can use a built-in module, or create your own to break up a large program

# print(help("modules"))
# print(help("math"))

# -----

# here are some ways to import 

# import math # imports EVERYTHING from the math module
# print(math.pi)

# import math as m # imports EVERYTHINg from math, but you can name the alias anything
# print(m.pi)

# from math import pi # imports pi from math. math does not work
# print(pi)

# -----

import example
print(example.pi)
squared_num = example.square(3)
cubed_num = example.cube(2)

print(squared_num, cubed_num, sep=", ")




