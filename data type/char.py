# Introduction to Character Data Type

# A character in Python is just a string of length 1
char_a = 'A'
char_b = 'b'

print("Character Data Type Example")
print("Character A:", char_a)
print("Character B:", char_b)


# Getting ASCII value of a character
print("ASCII value of A:", ord(char_a))
print("ASCII value of B:", ord(char_b))

# Getting character from ASCII value
print("Character for ASCII 97:", chr(97))
print("Character for ASCII 65:", chr(65))

# Checking if a character is uppercase or lowercase
if char_a.isupper():
    print(f"{char_a} is an uppercase letter.")
else:
    print(f"{char_a} is a lowercase letter.")

if char_b.islower():
    print(f"{char_b} is a lowercase letter.")
else:
    print(f"{char_b} is an uppercase letter.")

