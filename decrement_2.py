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


    if choice == "1":
        num = int(input("Enter a number to decrement: "))
        result = decrement_number(num)
        print(f"The result after decrementing {num} is: {result}")
    

    elif choice == "2":
        numbers = list(map(int, input("Enter a list of numbers to decrement (comma separated): ").split(',')))
        results = decrement_list(numbers)
        print(f"The result after decrementing each number in {numbers} is: {results}")
    

    elif choice == "3":
        start = int(input("Enter the starting number for the range: "))
        end = int(input("Enter the ending number for the range (should be less than the starting number): "))
        decrement_in_loop(start, end)
    

    else:
        print("Invalid choice. Please run the program again and select a valid option.")

if __name__ == "__main__":
    main()
