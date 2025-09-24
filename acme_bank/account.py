class Account:
    def __init__(self, account_type, balance=0.0 ):
        self.account_type = account_type
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance