import math

def logarithm_calculator():
    print("Logarithm Calculator")
    print("Choose a base for the logarithm:")
    print("1. Base 10 (common log)")
    print("2. Base e (natural log)")
    print("3. Custom base")
    try:
        choice = int(input("Enter your choice (1-3): "))

        if choice not in [1, 2, 3]:
            print("Invalid choice. Please select a valid option.")
            return

        number = float(input("Enter the number to calculate the logarithm: "))
        if number <= 0:
            print("Error: Logarithm is not defined for zero or negative numbers.")
            return
