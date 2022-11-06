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
print("-"*60)

# Total Votes
print(f"Total Votes: {len(ballotID)}")
print("-"*60)

# Percentage of Votes Based on Total Votes and Candidate Votes
print([f"Charles Casper Stockham: {round(((Charlie/len(ballotID))*100),3)}% ({Charlie}"])
print([f"Diana DeGette: {round(((Diana/len(ballotID))*100),3)}% ({Diana}"])
print([f"Raymon Anthony Doane: {round(((Raymon/len(ballotID))*100),3)}% ({Raymon}"])
print("-"*60)

# And the winner is
print(f"Winner: {winner}")
print("-"*60)
print('\n')

# Export Text File
outputpath=os.path.join("PyPoll","Analysis","poll_analysis.txt")

with open(outputpath, 'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-"*60])
    csvwriter.writerow([f"Total Votes: {len(ballotID)}"])
    csvwriter.writerow(["-"*60])
    csvwriter.writerow([f"Charles Casper Stockham: {round(((Charlie/len(ballotID))*100),3)}% ({Charlie}"])
    csvwriter.writerow([f"Diana DeGette: {round(((Diana/len(ballotID))*100),3)}% ({Diana}"])
    csvwriter.writerow([f"Raymon Anthony Doane: {round(((Raymon/len(ballotID))*100),3)}% ({Raymon}"])
    csvwriter.writerow(["-"*60])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-"*60])