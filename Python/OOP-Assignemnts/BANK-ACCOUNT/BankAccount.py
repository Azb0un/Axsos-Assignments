class BankAccount:
    def __init__(self, balance = 0, int_rate = 0.01):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance + 5:
            print("Insufficient funds")
        else:
            self.balance -= amount + 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        yi = self.balance * self.int_rate
        print("Your Interest Rate is:", yi)
        self.balance += (self.balance * self.int_rate)
        return self

Saving = BankAccount()
Running = BankAccount(int_rate= 0.05)

Saving.deposit(100).deposit(300).deposit(400).withdraw(300).yield_interest().display_account_info()

Running.deposit(500).deposit(1500).withdraw(250).withdraw(250).withdraw(250).withdraw(250).yield_interest().display_account_info()


