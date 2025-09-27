import csv

from customer import Customer

csv_file = "bank.csv"

if __name__ == "__main__":
    
    while True:
        choice = input("1) Add Customer 2) Login 3) Exit: ")
        if choice == "1":
            account_id = input("Enter account id: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            password = input("Enter password: ")
            new_customer = Customer(account_id, first_name, last_name, password)
            new_customer.save_to_csv()
            print(f"Customer added! {new_customer.first_name}")

        elif choice == "2":
            login_id = input("Enter your id: ")
            login_pass = input("Enter your password: ")
            logged_in_cus = None
            
            with open(csv_file, "r", newline="") as file:
                reader = csv.reader(file)
                header = next(reader)

                for row in reader:
                    if row[0] == login_id and row[3] == login_pass:
                        if row[4]:
                            checking_balance = float(row[4])
                        else:
                            checking_balance = 0.0
                        
                        if row[5]:
                            saving_balance = float(row[5])
                        else:
                            saving_balance = 0.0
                        
                        logged_in_cus = Customer(account_id=row[0], first_name=row[1], last_name=row[2], password=row[3], balance_checking = checking_balance, balance_savings = saving_balance)
                        break

            if logged_in_cus:
                print("welcome", logged_in_cus.first_name, logged_in_cus.last_name)
                while True:
                    user_input = input("(1) Deposit (2) Withdraw (3) open Checking (4) open Savings (5) Transfer (6) Exit ")

                    if user_input == "1":
                        account_type = input("From which account? (checking/savings): ").lower()
                        amount = float(input(f"Enter amount to deposit into : {account_type} "))
                        
                        with open(csv_file, "r", newline="") as file:
                            reader = csv.reader(file)
                            header = next(reader)
                            rows = list(reader)

                        for row in rows:
                            if row[0] == login_id:
                                if account_type == "checking":
                                    if row[4]:
                                        current_balance = float(row[4])
                                    else:
                                        current_balance = 0.0

                                    new_balance = current_balance + amount
                                    row[4] = str(new_balance)
                                    print(f"Deposit seccess your checking balance is: {new_balance}")

                                elif account_type == "savings":
                                    if row[5]:
                                        current_balance = float(row[5])
                                    else:
                                        current_balance = 0.0

                                    new_balance = current_balance + amount
                                    row[5] = str(new_balance)
                                    print(f"Deposit success new balance is: {row[5]}")
                    
                                with open(csv_file, "w", newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerow(header)
                                    writer.writerows(rows)
                                break
                        
                    elif user_input == "2":
                        account_type = input("From which account? (checking/savings): ").lower()
                        amount = float(input(f"Enter amount to withdraw form {account_type}: "))

                        new_balance = logged_in_cus.withdraw(login_id, amount, account_type)
                        if new_balance is not None:
                            print(f"Withdraw successful new {account_type} balance: {new_balance}")
                        else:
                            print("Withdraw failed insufficient funds")
                        

                    elif user_input == "3":
                        amount = float(input("Enter deposit amount for checking account: "))
                        new_balance = logged_in_cus.deposit(login_id, amount, "checking")
                        if new_balance is not None:
                            print(f"Checking account opened successfully Balance: {new_balance}")
                        

                    elif user_input == "4":
                        amount = float(input("Enter deposit amount for savings account: "))
                        new_balance = logged_in_cus.deposit(login_id, amount, "savings")
                        if new_balance is not None:
                            print(f"Savings account opened successfully Balance: {new_balance}")

                    elif user_input == "5":
                        print("1) transfer between my accounts")
                        print("2) transfer to customer")
                        tran_input = input("choose 1 or 2 : ")

                        if tran_input == "1":
                            print("1) checking to savings")
                            print("2) savings to checking")
                            to_input = input("choose 1 or 2 : ")
                            amount = float(input("Enter the amount to transfer: "))

                            if to_input == "1":
                                successful_tran = logged_in_cus.transfer_bet_my_accounts("checking", "savings", amount)
                            elif to_input == "2":
                                successful_tran = logged_in_cus.transfer_bet_my_accounts("savings", "checking", amount)
                            else:
                                print("invalid choice")
                                successful_tran = False

                        elif tran_input == "2":
                            from_account = input("Transfer from which account? (checking/savings):  ").lower()
                            target_id = input("Enter target customer id: ")
                            amount = float(input("Enter amount to transfer: "))
                            successful_tran = logged_in_cus.transfer_to_customer(from_account, target_id, amount)
                            
                        if successful_tran:
                            print(f"New checking balance: {logged_in_cus.checking_account.balance}")
                            print(f"New savings balance: {logged_in_cus.savings_account.balance}")    

                    elif user_input == "6":
                        print("Logged out")
                        break
                    else:
                        print("Invalide option!")
                    
            else:
                print("invalid id or password!")
            
        elif choice == "3":
            print("Exiting")
            break
        else:
            print("invalid choice!")

