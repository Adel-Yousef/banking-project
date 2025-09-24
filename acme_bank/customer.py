import csv

from account import Account


class Customer:
    def __init__(self, account_id, first_name, last_name, password, balance_checking=0, balance_savings=0):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.checking_account = Account("checking", balance_checking)
        self.savings_account = Account("savings", balance_savings)

    def save_to_csv(self, filename="bank.csv"):
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.account_id, self.first_name, self.last_name, self.password, self.checking_account.balance, self.savings_account.balance])

    def deposit(self, login_id, amount, account_type):
        if login_id != self.account_id:
            print("False customer id mismatch!")
            return None
        
        csv_file = "bank.csv"

        with open(csv_file, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)

        for row in rows:
            if row[0] == self.account_id:
                if account_type == "checking":
                    if row[4]:
                        current_balance = float(row[4])
                    else:
                        current_balance = 0.0

                    if current_balance > 0:
                        print("Checking account already exists!")
                        return None

                    new_balance = self.checking_account.deposit(amount)
                    row[4] = str(new_balance)
                    break
                elif account_type == "savings":
                    if row[5]:
                        current_balance = float(row[5])
                    else:
                        current_balance = 0.0
                    
                    if current_balance > 0:
                        print("Savings account already exists!")
                        return None
                    
                    new_balance = self.savings_account.deposit(amount)
                    row[5] = str(new_balance)
                    break
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        
        return new_balance



    
