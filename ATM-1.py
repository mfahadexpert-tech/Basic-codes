class BankAccount:
    # Static (class) variable
    __total_accounts = 0

    # Constructor
    def __init__(self, owner, account_no, initial_deposit):
        self.__owner = owner
        self.__account_no = account_no

        # Validate initial deposit
        if isinstance(initial_deposit, (int, float)) and initial_deposit >= 0:
            self.__balance = initial_deposit
        else:
            print("Invalid Initial Deposit! Balance set to 0.")
            self.__balance = 0

        # Increment total accounts
        BankAccount.__total_accounts += 1

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if isinstance(amount, (int, float)) and amount >= 0:
            self.__balance = amount
            print("Balance Updated Successfully.")
        else:
            print("Invalid Transaction Type")

    # Deposit Method
    def deposit(self, amount):
        if not isinstance(amount, (int, float)):
            print("Invalid Transaction Type")
            return

        if amount <= 0:
            print("Invalid Transaction Type")
            return

        self.__balance += amount
        print(f"Rs.{amount} Deposited Successfully.")

    # Withdraw Method
    def withdraw(self, amount):
        if not isinstance(amount, (int, float)):
            print("Invalid Transaction Type")
            return

        if amount <= 0:
            print("Invalid Transaction Type")
            return

        if amount > self.__balance:
            print("Transaction Declined")
        else:
            self.__balance -= amount
            print(f"Rs.{amount} Withdrawn Successfully.")

    # Display Account Details
    def display_account(self):
        print("\n------ Account Details ------")
        print("Owner      :", self.__owner)
        print("Account No :", self.__account_no)
        print("Balance    :", self.__balance)

    # Static Method
    @staticmethod
    def total_accounts():
        print("Total Accounts Created:", BankAccount.__total_accounts)


# ===============================
# Testing the Program
# ===============================

acc1 = BankAccount("Ali", "PK1001", 5000)

acc1.display_account()

print("\nCurrent Balance:", acc1.get_balance())

acc1.deposit(2000)
acc1.deposit(-100)
acc1.deposit("Hello")

acc1.withdraw(3000)
acc1.withdraw(10000)
acc1.withdraw("ABC")

acc1.set_balance(7000)
acc1.set_balance(-50)

print("\nFinal Balance:", acc1.get_balance())

acc1.display_account()

acc2 = BankAccount("Ahmed", "PK1002", 1000)

BankAccount.total_accounts()