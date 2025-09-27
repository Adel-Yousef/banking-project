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
    
    def withdraw(self, login_id, amount, account_type):
        if login_id != self.account_id:
            print("False customer id mismatch")
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
                        
                        if amount > current_balance:
                            print("insufficient funds")
                            return None
                        
                        new_balance = self.checking_account.withdraw(amount)
                        row[4] = str(new_balance)
                        break

                    elif account_type == "savings":
                        if row[5]:
                            current_balance = float(row[5])
                        else:
                            current_balance = 0.0
                        
                        if amount > current_balance:
                            print("insufficient funds")
                            return None
                        
                        new_balance = self.savings_account.withdraw(amount)
                        row[5] = str(new_balance)
                        break
            with open(csv_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(header)
                writer.writerows(rows)

            return new_balance

    def transfer_bet_my_accounts(self, from_account, to_account, amount):
        csv_file = "bank.csv"
        
        if from_account == "checking":
            if amount > self.checking_account.balance:
                print("Not enough money in checking account")
                return False
        else:  
            if amount > self.savings_account.balance:
                print("Not enough money in savings account")
                return False
        
        with open(csv_file, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)
        
        account_found = False
        
        for row in rows:
            if row[0] == self.account_id:

                account_found = True
                
                
                if from_account == "checking" and to_account == "savings":
                    if row[4]:
                        checking_balance = float(row[4])
                    else:
                        checking_balance = 0.0
                    
                    if row[5]:
                        savings_balance = float(row[5])
                    else:
                        savings_balance = 0.0
                    
                    new_checking = checking_balance - amount
                    new_savings = savings_balance + amount
                    
                    row[4] = str(new_checking)
                    row[5] = str(new_savings)

                    self.checking_account.balance = new_checking
                    self.savings_account.balance = new_savings
                
                elif from_account == "savings" and to_account == "checking":
                    if row[4]:
                        checking_balance = float(row[4])
                    else:
                        checking_balance = 0.0
                    
                    if row[5]:
                        savings_balance = float(row[5])
                    else:
                        savings_balance = 0.0
                    
                    new_savings = savings_balance - amount
                    new_checking = checking_balance + amount
                    
                    row[5] = str(new_savings)
                    row[4] = str(new_checking)

                    # here im updating the account object because in the current session the account balance is not updated and to prevent errors
                    self.savings_account.balance = new_savings
                    self.checking_account.balance = new_checking
                
                break
        
        if not account_found:
            print("Our account was not found in CSV!")
            return False
        
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        
        print(f"Transfer {amount} from {from_account} to {to_account} successful!")
        return True   

    def transfer_to_customer(self, from_account, target_account_id, amount):
        csv_file = "bank.csv"

        if from_account == "checking":
            if amount > self.checking_account.balance:
                print("Not enough money in checking account")
                return False
        else:
            if amount > self.savings_account.balance:
                print("Not enough money in savings account")
                return False
        
        with open(csv_file, "r", newline="") as file:
            reader = csv.reader(file)
            header = next(reader)
            rows = list(reader)

        target_found = False

        for row in rows:
            if row[0] == target_account_id:
                target_found = True

                if row[4]:
                    target_balance = float(row[4])
                else:
                    target_balance = 0.0

                row[4] = str(target_balance + amount)
                break

        for row in rows:
            if row[0] == self.account_id:
                if from_account == "checking":
                    if row[4]:
                        current_balance = float(row[4])
                    else:
                        current_balance = 0.0
                        
                    new_balance = current_balance - amount
                    row[4] = str(new_balance)

                    self.checking_account.balance = new_balance
                else:
                    if row[5]:
                        current_balance = float(row[5])
                    else:
                        current_balance = 0.0
                        
                    new_balance = current_balance - amount
                    row[5] = str(new_balance)

                    self.savings_account.balance = new_balance
                break

        if not target_found:
            print(f"customer id {target_account_id} not found")
            return False
        
        with open(csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(rows)
        
        print(f"Transfer successful {amount} sent to {target_account_id}")
        return True