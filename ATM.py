pin = "1234"
balance = 5000

entered_pin = input("Enter PIN: ")

if entered_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            if amount > 0:
                balance += amount
                print("Updated balance:", balance)
            else:
                print("Invalid amount")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount")
            elif amount <= balance:
                balance -= amount
                print("Please collect your cash")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance")

        elif choice == "4":
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong PIN. Access denied.")