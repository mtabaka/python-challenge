import os
import csv
from collections import Counter

election_data_csv = os.path.join("election_data.csv")
election_data_results = os.path.join("PyPoll_Results.txt")

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    votes = Counter()
    candidates = []
    percentage = []
    answer = []
    
    for row in csvreader:
        candidates.append(row[2])

    total_votes = len(candidates)    

    for name in candidates:
        votes[name] += 1

    winner = max(zip(votes.values(), votes.keys()))
    names = tuple(votes.keys())
    votes = tuple(votes.values())

    for x in votes:
        percentage.append((int(x)/total_votes)*100)

    answer.append("Election Results")
    answer.append("----------------")
    answer.append("Total Votes:  " + str(total_votes))
    for x in range(len(names)):
        answer.append(names[x] + ":" + str(round(percentage[x],1)) + "%" + "(" + str(votes[x]) + ")")

    answer.append("Winner: " + winner[1])

    print("\n".join((answer)))

    print("\n".join((answer)))

with open(election_data_results, "w") as txtfile:
    txtfile.write("\n".join(answer))
    

    
    
    





    
    
    






    
