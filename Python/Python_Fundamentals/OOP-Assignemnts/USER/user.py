class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def display_user_balance(self):
        print(self.account_balance)

    def make_deposit(self,amount):
        self.account_balance = self.account_balance + amount

    def make_withdrawal(self, amount):
        if amount > self.account_balance:
            print("You Dont Have Enough Money")
        else:
            self.account_balance = self.account_balance - amount
        

    def transfer_money(self, other_user, amount):
        if amount > self.account_balance:
            print("You Dont Have Enough Money")
        else:
            self.account_balance -= amount
            other_user.account_balance += amount


Alli = User("Alli", "a@gmail.com")
Nasri = User("Nasri", "n@gmail.com")
Fatima = User("Fatima", "f@gmail.com")
Alli.display_user_balance()
Nasri.display_user_balance()
Fatima.display_user_balance()

print()

Alli.make_deposit(200)
Alli.make_deposit(300)
Alli.make_deposit(500)
Alli.make_withdrawal(400)
Alli.display_user_balance()

print()

Nasri.make_deposit(400)
Nasri.make_deposit(400)
Nasri.make_withdrawal(100)
Nasri.make_withdrawal(200)
Nasri.display_user_balance()

print()

Fatima.make_deposit(1000)
Fatima.make_withdrawal(300)
Fatima.make_withdrawal(300)
Fatima.make_withdrawal(300)
Fatima.display_user_balance()

print()

Alli.transfer_money(Fatima, 100)
Alli.display_user_balance()
Fatima.display_user_balance()