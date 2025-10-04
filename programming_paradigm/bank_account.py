class BankAccount:

    def __init__(self):
        self.deposit = 0

    def deposit(self, amount):
        if amount > 0:
            self.deposit += amount
            print(f"Deposited: ${self.amount}.")
        else:
            print("Deposit must be positive")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive")
        else:
            self.balance -= amount
            print(f"withdrew: ${amount}")

    def display(self):
        print(f"Current Balance: ${self.balance}")
