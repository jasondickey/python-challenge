import os
import csv
import numpy as n

# define paths for incoming and outgoing files
file1 = os.path.join("budget_data_1.csv")
file2 = os.path.join("budget_data_2.csv")
output_path = os.path.join('new.txt')

# read incoming files
csv_file1 = csv.reader(open(file1))
csv_file2 = csv.reader(open(file2))

# define lists and varibles
date = []
rev = []
total_rev = 0

# read through each file
for row in csv_file1:

    #insert column one into date list
    date.append(row[0])

    #insert  column two into revenue list
    revenue = row[1]

    # replace non-integer values with 0 for revenue list
    try:
        revenue = int(revenue)
    except ValueError:
        revenue = 0
    
    # add values in revenue list with each pass
    total_rev += revenue
    rev.append(revenue)

# create list of dates and sum total revenue for list 2
for row in csv_file2:

    date.append(row[0])
    revenue = row[1]

    # replace non-integer values with 0, and add values to revenue list
    try:
        revenue = int(revenue)
    except ValueError:
        revenue = 0

    total_rev += revenue
    rev.append(revenue)

# set date and rev lists as arrays in order to use index
d = n.array(date)
r = n.array(rev)

# identify min and max values of revenue, and locate their indexes
idmx = n.where(r==r.max())[0]
idmn = n.where(r==r.min())[0]

print("Financial Analysis")
print("------------------")
print("Total Months: " + str(len(date)-2))
print("Total Revenue: $" + str(total_rev))
print("Average Revenue: $" + str(int(total_rev/len(date))))
print("Greatest Increase in Revenue: " + str(d[int(idmx)]) + " ($" + str(r[int(idmx)]) + ")")  
print("Greatest Decrease in Revenue: " + str(d[int(idmn)]) + " ($" + str(r[int(idmn)]) + ")") 

# Initialize csv.writer and write file output
with open(output_path, 'w', newline='') as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------"])
    csvwriter.writerow(["Total Months: " + str(len(date)-2)])
    csvwriter.writerow(["Total Revenue: $" + str(total_rev)])
    csvwriter.writerow(["Average Revenue: $" + str(int(total_rev/len(date)))])
    csvwriter.writerow(["Greatest Increase in Revenue: " + str(d[int(idmx)]) + " ($" + str(r[int(idmx)]) + ")"])  
    csvwriter.writerow(["Greatest Decrease in Revenue: " + str(d[int(idmn)]) + " ($" + str(r[int(idmn)]) + ")"]) 