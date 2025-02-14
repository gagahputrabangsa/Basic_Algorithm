# Introduction to Boolean Data Type

# Boolean values: True or False
is_raining = True
is_sunny = False

print("Boolean Data Type Example")
print("Is it raining?", is_raining)
print("Is it sunny?", is_sunny)

# Boolean expressions
print("5 > 3:", 5 > 3)  # True
print("10 == 20:", 10 == 20)  # False

# Using Boolean in conditions
if is_raining:
    print("Don't forget to take an umbrella!")
else:
    print("Enjoy the clear weather!")

# Getting user input and converting it to Boolean
daylight = input("Is it daylight? (yes/no): ").strip().lower() == "yes"

if daylight:
    print("It's bright outside!")
else:
    print("It's dark outside!")

