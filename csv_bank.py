import csv

data = [
    ["account_id","frst_name","last_name","password","balance_checking","balance_savings"],
    [10001,"suresh","sigera","juagw362",1000,10000],
    [10002,"james","taylor","idh36%@#FGd",10000,10000],
    [10003,"melvin","gordon","uYWE732g4ga1",2000,20000],
    [10004,"stacey","abrams","DEU8_qw3y72$",2000,20000],
    [10005,"jake","paul","d^dg23g)@",100000,100000],
]

# Use w to overwrite a file, use a to append to a file (w is probably fine)
with open('bank.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Reading from a CSV file
with open('bank.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])