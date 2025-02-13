# Introduction to Floating-Point Numbers in Python

# Floating-point numbers (floats) represent decimal values
a = 5.5  # A float number
b = 2.3  # Another float number

# Basic arithmetic operations with floats
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

# Printing results
print("Floating Point Operations:")
print(f"{a} + {b} = {addition}")
print(f"{a} - {b} = {subtraction}")
print(f"{a} * {b} = {multiplication}")
print(f"{a} / {b} = {division}")

# Demonstrating float precision issue
print("\nFloat Precision Issue:")
num1 = 0.1 + 0.2
print("0.1 + 0.2 =", num1)  # Might print 0.30000000000000004 due to floating-point precision

# Converting between float and integer
c = 10   # Integer
float_c = float(c)  # Convert int to float
int_a = int(a)  # Convert float to int (truncates the decimal part)

print("\nType Conversions:")
print(f"Integer {c} converted to float: {float_c}")
print(f"Float {a} converted to integer: {int_a}")

