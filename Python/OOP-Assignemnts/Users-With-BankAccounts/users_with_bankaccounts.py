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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.saving_account = BankAccount(balance=500)
        self.running_account = BankAccount(balance=3000, int_rate=0.02)

Alli = User("Alli", "a@gmail.com")

Alli.saving_account.yield_interest().display_account_info()
Alli.running_account.yield_interest().display_account_info()
