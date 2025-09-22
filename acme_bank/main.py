from customer import Customer

if __name__ == "__main__":
    account_id = input("Enter account id: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    password = input("Enter password: ")

    new_customer = Customer(account_id, first_name, last_name, password)
    new_customer.save_to_csv()
    print(f"Customer added! {new_customer.first_name}")
