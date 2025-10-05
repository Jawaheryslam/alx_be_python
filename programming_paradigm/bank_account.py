class BankAccount:

    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.deposit += amount
            print(f"Deposited: ${amount}.")
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"withdrew: ${amount}")

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
