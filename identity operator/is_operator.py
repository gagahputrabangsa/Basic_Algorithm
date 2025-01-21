# Example for 'is' operator
# Define two variables
a = [1, 2, 3]
b = a  # b refers to the same object as a
c = [1, 2, 3]  # c is a different object with the same content

# Check if a and b refer to the same object
print(f"a is b: {a is b}")  # True because b is the same object as a

# Check if a and c refer to the same object
print(f"a is c: {a is c}")  # False because c is a different object
