import os
import csv

data1 = os.path.join("budget_data_1.csv")
data2 = os.path.join("budget_data_2.csv")

# Lists to store data
date = []
revenue = [0,0]

with open(data1, newline="") as csvfile1:
    csvreader= csv.reader(csvfile1, delimiter=",")
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add revenue
        revenue.append(row[1])

with open(data2, newline="") as csvfile2:
    csvreader= csv.reader(csvfile2, delimiter=",")
    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add revenue
        revenue.append(row[1])

numberofmonths = len(date)



print("Financial Analysis")
print("------------------")
print("Total Months: " + str(numberofmonths))
print("Total Revenue: $" + str(sum(int(revenue))))
print("Average Revenue: ")
print("Greatest Increase in Revenue: ")  
print("Greatest Decrease in Revenue: ")