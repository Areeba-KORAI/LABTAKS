balance = 50000

while True:
  print("\n--- ATM Menu ---")
  print("1. Check Balance")
  print("2. Deposit")
  print("3. Withdraw")
  print("4. Exit")

  choice = input("Select an option (1-4): ")

  if choice == "1":
    print(f"Current Balance: {balance}")
  elif choice == "2":
    amount = float(input("Enter deposit amount: "))
    balance += amount
    print(f"Deposited {amount}. New Balance: {balance}")
  elif choice == "3":
    amount = float(input("Enter withdrawal amount: "))
    if amount <= balance:
      balance -= amount
      print(f"Withdrawn {amount}. New Balance: {balance}")
    else:
      print("Insufficient balance!")
  elif choice == "4":
    print("Thank you for using the ATM. Goodbye!")
    break
  else:
    print("Invalid choice. Please select between 1 and 4.")