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

    def transfer_from_saving_to_running(self, amount):
        self.saving_account.withdraw(amount - 5)
        self.running_account.deposit(amount)

    def transfer_from_running_to_saving(self, amount):
        self.running_account.withdraw(amount - 5)
        self.saving_account.deposit(amount)



Alli= User("Alli", "a@gmail.com")
Fatima = User("Fatima", "f@gmail.com")

Alli.saving_account.display_account_info()
Alli.running_account.display_account_info()

Alli.transfer_from_saving_to_running(200)


Alli.saving_account.display_account_info()
Alli.running_account.display_account_info()

Alli.transfer_from_running_to_saving(3000)

Alli.saving_account.display_account_info()
Alli.running_account.display_account_info()