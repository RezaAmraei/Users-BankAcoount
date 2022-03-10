class BankAccount:
    def __init__(self,int_rate = 0.01, balance = 0 ):
        self.balance = balance
        self.intrest_rate = int_rate
    
    def deposit(self, balance):
        self.balance += balance
        return self

    def withdraw(self, balance):
        if self.balance - balance >= 0:
            self.balance -= balance
        else:
            print('insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        print("Balance: ",self.balance)
        return self

    def yield_intrest(self):
        if self.balance >= 0:
            self.balance += self.intrest_rate * self.balance
            return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print("User's Balance: ", self.account.balance)
        return self

reza = User("Reza", "amraeireza@gmail.com")
reza.display_user_balance().make_deposit(100).display_user_balance().make_withdraw(50).display_user_balance().make_withdraw(200).display_user_balance()
