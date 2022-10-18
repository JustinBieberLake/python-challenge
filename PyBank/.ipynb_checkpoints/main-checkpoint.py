import os
import csv

budget_data=os.path.join('.','Resources','budget_data.csv')

with open(budget_data) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header =next(csvfile)
    print(f"Header:{csv_header}")

    for row in csv_reader:
        print(row)
        print(row[0],row[1])

print('\n'"-"*75,'\n')
