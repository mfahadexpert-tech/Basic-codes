#Ek Wallet class banayein. Jab bhi naya wallet object bane
# 
# , __init__ constructor automatically
#chalna chahiye aur starting balance 0 set karna chahiye.

class Wallet:
    def __init__(self):
        self.balance = 0
wallet = Wallet()
print("Balance:", wallet.balance)