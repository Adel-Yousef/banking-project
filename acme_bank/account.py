class Account:
    def __init__(self, account_type, balance=0.0 ):
        self.account_type = account_type
        self.balance = balance
        self.overdraft_count = 0  # this to count the successful overdraft
        self.failed_overdraft_count = 0  # this to count failed overdraft
        self.is_active = True
        
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return None