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
        if choice == 1:
            result = math.log10(number)
            print(f"The base-10 logarithm of {number} is {result:.4f}")
        elif choice == 2:
            result = math.log(number)
            print(f"The natural logarithm of {number} (base e) is {result:.4f}")
        elif choice == 3:
            base = float(input("Enter the base for the logarithm: "))
            if base <= 0 or base == 1:
                print("Error: Logarithm base must be greater than 0 and not equal to 1.")
            else:
                result = math.log(number, base)
                print(f"The logarithm of {number} to the base {base} is {result:.4f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
# Run the logarithm calculator
logarithm_calculator()
