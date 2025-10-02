class BankAccount:
    def __init__(self, deposit, withdraw, display):
        self.deposit = deposit
        self.withdraw = withdraw
        self.display = display

    def account_balance(self):
        account_balance += deposit
        return deposit

    def deposit(self, amount):
        if amount > 0:
            self.deposit += amount
            print(f"balance: ${self.deposit}.")
        else:
            print("Deposit must be positive")

    def withdraw(self):
        if withdraw > deposit:
            print("Insufficient funds.")
        else:
            print(f"withdraw: ${self.withdraw}")

    def display(self):
        display = f"{deposit} - {withdraw}"
        print(f"Current Balance: ${self.display}")
