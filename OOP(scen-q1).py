class BankAccount:

    def __init__(self):
        self.__balance = 0

    def set_balance(self, amount):

        if isinstance(amount, (int, float)):

            if amount > 0:
                self.__balance = amount

            else:
                print("Error: Balance must be positive.")

        else:
            print("Error: Balance must be int or float.")

    def get_balance(self):
        return self.__balance


account = BankAccount()

account.set_balance(15000)

print("Current Balance:", account.get_balance())
#print(account._BankAccount__balance) 