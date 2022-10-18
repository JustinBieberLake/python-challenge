import os
import csv
print(os.getcwd())
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None) 

    csv_header =next(csvfile)
    print(f"Header:{csv_header}")

    for row in csvreader:
        print(row)
        print(row[0],row[1])

print('\n'"-"*75,'\n')
