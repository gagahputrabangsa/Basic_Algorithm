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
    

    # User input as string
    user_input = input("Enter your favorite programming language: ")
    print("You entered:", user_input)
    
    # Checking string membership
    if "Python" in message:
        print("'Python' is found in the message!")
    else:
        print("'Python' is not found in the message.")

if __name__ == "__main__":
    main()
