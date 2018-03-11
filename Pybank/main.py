import os
import csv
import numpy as n

# define file paths
file1 = os.path.join("budget_data_1.csv")
file2 = os.path.join("budget_data_2.csv")

output_path = os.path.join('new.txt')

# read files
csv_file1 = csv.reader(open(file1))
csv_file2 = csv.reader(open(file2))

# define lists and varibles
date = []
rev = []
total_rev = 0

# create list of dates and sum total revenue for list 1
for row in csv_file1:
    date.append(row[0])
    revenue = row[1]

    # replace non-integer values with 0
    try:
        revenue = int(revenue)
    except ValueError:
        revenue = 0
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


d = n.array(date)
r = n.array(rev)

idmx = n.where(r==r.max())[0]
idmn = n.where(r==r.min())[0]

print("Financial Analysis")
print("------------------")
print("Total Months: " + str(len(date)-2))
print("Total Revenue: $" + str(total_rev))
print("Average Revenue: $" + str(int(total_rev/len(date))))
print("Greatest Increase in Revenue: " + str(d[int(idmx)]) + " ($" + str(r[int(idmx)]) + ")")  
print("Greatest Decrease in Revenue: " + str(d[int(idmn)]) + " ($" + str(r[int(idmn)]) + ")") 


with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["------------------"])
    csvwriter.writerow(["Total Months: " + str(len(date)-2)])
    csvwriter.writerow(["Total Revenue: $" + str(total_rev)])
    csvwriter.writerow(["Average Revenue: $" + str(int(total_rev/len(date)))])
    csvwriter.writerow(["Greatest Increase in Revenue: " + str(d[int(idmx)]) + " ($" + str(r[int(idmx)]) + ")"])  
    csvwriter.writerow(["Greatest Decrease in Revenue: " + str(d[int(idmn)]) + " ($" + str(r[int(idmn)]) + ")"]) 