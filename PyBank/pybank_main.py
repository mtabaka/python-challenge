import os 
import csv

budget_csv = os.path.join("budget_data.csv")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    months_count= list(csvreader)
    row_count = len(months_count)
    print("Total Months: " + str(len(months_count)))

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    total = 0
    for row in csvreader:
        sum_money = int(row[1])
        total = total + sum_money
    print("Total: $" + str(total))    