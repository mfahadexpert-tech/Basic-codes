balance = 5000

withdrawal_amount = int(input("Enter withdrawal amount: "))

if withdrawal_amount > balance:
    print("Insufficient Funds")
else:
    balance = balance - withdrawal_amount
    print("Remaining Balance:", balance)