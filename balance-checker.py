#Aik balance variable rakhen. User se withdraw amount lein. Agar amount balance se kam ya barabar ho to "Success" print karein, warna "Insufficient Balance"
balance=1000
amount=int(input("Enter the amount to withdraw: "))
if amount<=balance:
    balance-=amount
    print(f"successfullt withrawn {amount} remaining balance is {balance}")
else:
    print("insufficient balance")




   
