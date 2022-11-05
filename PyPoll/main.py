import os
import csv

csvpath=os.path.join("PyPoll","Resources","election_data.csv")

ballotID=[]
candidate=[]
Charlie=0
Diana=0
Raymon=0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile)

    # Header
    csvheader=next(csvreader)

    # Column List
    for row in csvreader:
        ballotID.append(row[0])
        candidate.append(row[2])
    
    # Number of Votes per Candidate
    for i in range(len(candidate)):
        if candidate[i]=="Charles Casper Stockham":
            Charlie=Charlie+1
        elif candidate[i]=="Diana DeGette":
            Diana=Diana+1
        elif candidate[i]=="Raymon Anthouny Doane":
            Raymon=Raymon+1

    # Who Had the Most Votes
    if Charlie>Diana and Charlie>Raymon:
        winner="Charles Casper Stockham"
    elif Diana>Charlie and Diana>Raymon:
        winner="Diana DeGette"
    elif Raymon>Charlie and Raymon>Diana:
        winner="Raymon Anthony Doane"

print('\n')
print("Election Results")
print("-"*40)

# Total Votes
print(f"Total Votes: {len(ballotID)}")
print("-"*40)
# 