import csv

class Customer:
    def __init__(self, account_id, first_name, last_name, password):
        self.account_id = account_id
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_to_csv(self, filename="bank.csv"):
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([self.account_id, self.first_name, self.last_name, self.password, 0, 0])
