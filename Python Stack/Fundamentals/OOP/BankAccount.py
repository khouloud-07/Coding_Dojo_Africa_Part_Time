
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

Account_1 = BankAccount(0.02, 200)
Account_2 = BankAccount(0.04, 300)

Account_1.deposit(50).deposit(100).deposit(70).withdraw(200).yield_interest().display_account_info()
Account_2.deposit(1000).deposit(280).withdraw(900).withdraw(20).withdraw(10).withdraw(40).yield_interest().display_account_info()

BankAccount.print_all_accounts()
