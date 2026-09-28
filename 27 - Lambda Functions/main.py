# lambda function -> a small, anonymous function intended for a one time use (throw-away function)
#                    They take any number of arguments, but only have one expression
#                    They help keep the namespace clean and is useful with higher order functions, like
#                    sort(), map(), filter() and reduce()

#                    lambda parameters: expression


# Some examples
# NOTE: These aren't great examples. Realistically, you can just write the statement when assigning the variable
double = lambda x: x * 2
add = lambda x, y: x + y
max_value = lambda x, y: x  if x > y  else y
min_value = lambda x, y: x  if x < y  else y
full_name = lambda first, last: first + " " + last
is_even = lambda x: x % 2 == 0
age_check = lambda age: True if age >= 18 else False


print(double(2))
print(add(2, 3))
print(max_value(10, 25))
print(min_value(10, 25))
print(full_name("Dylan", "Ryan"))
print(is_even(2))
print(age_check(17))
