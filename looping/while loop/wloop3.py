# Introduction message
print("Welcome to the Number Guessing Game!")

# Ask the user for the range of numbers to guess
lower_bound = int(input("Enter the lower bound for the number range: "))
upper_bound = int(input("Enter the upper bound for the number range: "))

# Generate a secret number to guess within the given range
import random
secret_number = random.randint(lower_bound, upper_bound)

# Initialize the number of attempts and a flag for the correct guess
attempts = 0
guessed_correctly = False

# Start the while loop for the guessing game
while not guessed_correctly:
    # Increment the number of attempts
    attempts += 1
    
    # Ask the user to guess the number
    user_guess = int(input(f"Attempt {attempts}: Guess the number between {lower_bound} and {upper_bound}: "))
    
    # Check if the guess is correct, too low, or too high
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
        else:
        guessed_correctly = True
        print(f"Congratulations! You've guessed the correct number {secret_number} in {attempts} attempts.")

# Final message
print("Thank you for playing the Number Guessing Game!")

