#simple banking system
balance = 1000  # Initial balance

while True:
    print("\n==== Simple Banking System ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        print(f"Your current balance is: ${balance}")
    
    elif choice == '2':
        amount = input("Enter deposit amount: ")
        if amount.isdigit() and int(amount) > 0:
            balance += int(amount)
            print(f"Successfully deposited ${amount}. New balance: ${balance}")
        else:
            print("Invalid amount. Please enter a positive number.")
    
    elif choice == '3':
        amount = input("Enter withdrawal amount: ")
        if amount.isdigit() and int(amount) > 0:
            if int(amount) <= balance:
                balance -= int(amount)
                print(f"Successfully withdrew ${amount}. Remaining balance: ${balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Please enter a positive number.")
