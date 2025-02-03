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

