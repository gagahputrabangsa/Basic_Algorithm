
# Example to demonstrate the 'is not' operator

# Define two variables
a = [1, 2, 3]

b = a  # b refers to the same object as a

c = [1, 2, 3]  # c is a different object with the same content

# Check if a and c do not refer to the same object
print(f"a is not c: {a is not c}")  # True because c is a different object

# Check if a and b do not refer to the same object
print(f"a is not b: {a is not b}")  # False because b is the same object as a
