def decrement_number(number):
    """Decrements a single number."""
    return number - 1

def decrement_list(numbers):
    """Decrements each number in the list."""
    return [number - 1 for number in numbers]

def decrement_in_loop(start, end):
    """Decrements numbers in a range and prints each value."""
    for number in range(start, end, -1):
        print(f"Decrementing: {number}")

def main():
    print("Welcome to the Decrement Program!")
    
    # Get user input for a single number
    choice = input("Do you want to decrement a single number (1), a list of numbers (2), or a range (3)? Enter 1, 2, or 3: ")


