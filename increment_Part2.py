# Extended Increment Program

def increment_number(number):
    """Function to increment a number by 1."""
    return number + 1

def reset_number():
    """Function to reset the number to 0."""
    return 0

def display_menu():
    """Display the menu options to the user."""
    print("\nMenu:")
    print("1. Increment the number")
    print("2. Reset the number")
    print("3. Exit")

def main():
    print("Welcome to the Increment Program!")
    current_number = 0  # Initial number
    print(f"Starting number: {current_number}")
    

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                current_number = increment_number(current_number)
                print(f"Current number after increment: {current_number}")
            elif choice == 2:
                current_number = reset_number()
                print("The number has been reset to 0.")
            elif choice == 3:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
