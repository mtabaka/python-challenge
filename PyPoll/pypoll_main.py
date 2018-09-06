import os
import csv
from collections import Counter

election_data_csv = os.path.join("election_data.csv")

with open(election_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    total_votes = list(csvreader)
    row_count = len(total_votes)
    print("Total Votes: " + str(len(total_votes)))






    
    
    






    
