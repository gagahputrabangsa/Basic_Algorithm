

# Input a number from the user
number = int(input("Enter a number: "))
shift_amount = int(input("Enter the number of positions to shift right: "))
# Perform the right shift
shifted_result = number >> shift_amount

# Display the result
print(f"Result of {number} >> {shift_amount} is {shifted_result}")

