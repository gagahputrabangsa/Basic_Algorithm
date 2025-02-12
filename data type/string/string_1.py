# Introduction to String Data Type in Python

def main():
    # Defining a string
    message = "Hello, welcome to the world of Python!"
    print("Original message:", message)
    
    # String concatenation
    name = "Alice"
    greeting = "Hello, " + name + "!"
    print("Concatenated string:", greeting)
    
    # String length
    print("Length of message:", len(message))
    
    # String slicing
    print("First five characters:", message[:5])
    print("Last five characters:", message[-5:])
    
    # String methods
    print("Uppercase:", message.upper())
    print("Lowercase:", message.lower())
    print("Replaced word:", message.replace("Python", "Programming"))
    

