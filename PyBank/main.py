# Imports
import os
import csv

# Link Data
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

totalmonths=[]
nettotal=[]
profitlosses=[]
rowcount=0

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile)
    
    # Header
    csvheader=next(csvfile)

    # Lists for Columns
    for row in csvreader:
        totalmonths.append(row[0])
        nettotal.append(int(row[1]))
    # New list for profit/losses
    for i in range(len(totalmonths)-1):
        profitlosses.append(int(nettotal[i+1]-nettotal[i]))

# Print
print('\n')
print("Financial Analysis")
print("-"*50)
# Total Months
print(f"Total Months: {len(totalmonths)}")
# Net Total
print(f"Total: ${sum(nettotal)}")
# Average Change
print(f"Average Change: ${int(sum(profitlosses)/(len(profitlosses)))}")
# Month With the Greatest Increase
print(f"Greatest Increase in Profits: {totalmonths[profitlosses.index(max(profitlosses))+1]} (${max(profitlosses)})")
# Month With Greatest Decrease
print(f"Greatest Decrease in Profits: {totalmonths[profitlosses.index(min(profitlosses))+1]} (${min(profitlosses)})")
print('\n')

# Export Text File
outputpath=os.path.join("PyBank","Analysis", "budget_analysis.txt")
with open (outputpath, 'w') as csvfile:
    csvwriter=csv.writer(csvfile)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(["-"*50])
    csvwriter.writerow([f"Total Months: {len(totalmonths)}"])
    csvwriter.writerow([f"Total: ${sum(nettotal)}"])
    csvwriter.writerow([f"Average Change: ${int(sum(profitlosses)/(len(profitlosses)))}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {totalmonths[profitlosses.index(max(profitlosses))+1]} (${max(profitlosses)})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {totalmonths[profitlosses.index(min(profitlosses))+1]} (${min(profitlosses)})"])