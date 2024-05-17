class BankAccount:
    # don't forget to add some default values for these parameters!
    #! Constructor
    accounts = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else :
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        while self.balance > 0 :
            self.balance += (self.balance*self.int_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User (BankAccount):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(100)
        return self
    def make_withdrawl(self, amount):
        self.account.withdraw(200)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self


Account_1 = User("khouloud", "khouloud@gmail.com")
Account_1.make_deposit(200).make_withdrawl(150).display_user_balance()


Account_1.deposit(50).deposit(100).deposit(70).withdraw(200).yield_interest().display_account_info()
BankAccount.print_all_accounts()