import os
import csv
from statistics import mean

budget_csv = os.path.join("budget_data.csv")
budget_data_results = os.path.join("PyBank_Results.txt")

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    storage = {}
    monthChange = []
    final = {}
    answer = []

    for row in csvreader:
        if row[0] != "Date":
            storage[row[0]] = int(row[1])

totalMonth = len(storage)
totalRevenue = sum(storage.values())
revs = tuple(storage.values())
month = tuple(storage.keys())

for x in range(1, (len(revs))):
    monthChange.append((int(revs[x]) - int(revs[x-1])))

average = round(mean(monthChange))

for x in range(1, (len(month))):
    final[month[x]] = int(monthChange[x-1])

    maxIncrease = max(zip(final.values(), final.keys()))
    minDecrease = min(zip(final.values(), final.keys()))

    answer.append('Financial Analysis')
    answer.append('----------------------------')
    answer.append('Total Months: ' + str(totalMonth))
    answer.append('Total Revenue: $' + str(totalRevenue))
    answer.append('Average Revenue Change: $' + str(average))
    answer.append('Greatest Increase in Revenue: ' + str(maxIncrease[1]) + ' ($' + str(maxIncrease[0]) + ')')
    answer.append('Greatest Decrease in Revenue: ' + str(minDecrease[1]) + ' ($' + str(minDecrease[0]) + ')')

    
    print("\n".join((answer)))
    with open(budget_data_results, "w") as txtfile:
        txtfile.write("\n".join(answer))