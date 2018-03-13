import os
import csv
import numpy as n

# define paths for incoming and outgoing files
file1 = os.path.join("election_data_1.csv")
file2 = os.path.join("election_data_2.csv")
output_path = os.path.join('new.txt')

# build varibles to be used later
Candidate = []
Candidate_p = []
Candidate_d = []
Candidate_scores = {}
Cordin = 0
Vestal = 0
Torres = 0
Seth = 0
Correy = 0
Li = 0
Otooley = 0
Khan = 0
Total = 0

# establish candidate names -- this was done via multiple iterations after file was imported into a list. The lists distinct values were identified
Candidate_1 = "Cordin"
Candidate_2 = "Vestal"
Candidate_3 = "Torres"
Candidate_4 = "Seth"
Candidate_5 = "Correy"
Candidate_6 = "Li"
Candidate_7 = "O'Tooley"
Candidate_8 = "Khan"

# build varibles for %
Candidate_1_p = 0
Candidate_2_p = 0
Candidate_3_p = 0
Candidate_4_p = 0
Candidate_5_p = 0
Candidate_6_p = 0
Candidate_7_p = 0
Candidate_8_p = 0

# open both files and read them
csv_file1 = csv.reader(open(file1))
csv_file2 = csv.reader(open(file2))

    # Loop through the data for file 1
for row in csv_file1:
        # add each candidate row into a list
    Candidate.append(row[2])
    
    # Loop through the data for file 2
for row in csv_file2:
        # add candidates from 2nd file to list
    Candidate.append(row[2])        

# find total number of votes for each candidate and calc total
Cordin = Candidate.count(Candidate_1)
Vestal = Candidate.count(Candidate_2)
Torres = Candidate.count(Candidate_3)
Seth = Candidate.count(Candidate_4)
Correy = Candidate.count(Candidate_5)
Li = Candidate.count(Candidate_6)
Otooley = Candidate.count(Candidate_7)
Khan = Candidate.count(Candidate_8)
Total = Cordin + Vestal + Torres + Seth + Correy + Otooley + Khan

# calculate the percentage for each candidate
Candidate_1_p = Cordin/Total
Candidate_2_p = Vestal/Total
Candidate_3_p = Torres/Total
Candidate_4_p = Seth/Total
Candidate_5_p = Correy/Total
Candidate_6_p = Li/Total
Candidate_7_p = Otooley/Total
Candidate_8_p = Khan/Total

# build list of all candidate percentages
Candidate_p.append(Candidate_1_p)
Candidate_p.append(Candidate_2_p)
Candidate_p.append(Candidate_3_p)
Candidate_p.append(Candidate_4_p)
Candidate_p.append(Candidate_5_p)
Candidate_p.append(Candidate_6_p)
Candidate_p.append(Candidate_7_p)
Candidate_p.append(Candidate_8_p)

# build list of call candidates
Candidate_d.append(Candidate_1)
Candidate_d.append(Candidate_2)
Candidate_d.append(Candidate_3)
Candidate_d.append(Candidate_4)
Candidate_d.append(Candidate_5)
Candidate_d.append(Candidate_6)
Candidate_d.append(Candidate_7)
Candidate_d.append(Candidate_8)

# create dictionary with percentage as key, and candidate name as value
Candidate_scores = dict(zip(Candidate_p,Candidate_d))

# print results of election
print("Election Results")
print("----------------")
print("Total Votes: " + str(Total))
print("----------------")
print(Candidate_1 + ": " + str('{:.1%} '.format(Candidate_1_p)) + "(" +str(Cordin) + ")")
print(Candidate_2 + ": " + str('{:.1%} '.format(Candidate_2_p)) + "(" +str(Vestal) + ")")
print(Candidate_3 + ": " + str('{:.1%} '.format(Candidate_3_p)) + "(" +str(Torres) + ")")
print(Candidate_4 + ": " + str('{:.1%} '.format(Candidate_4_p)) + "(" +str(Seth) + ")")
print(Candidate_5 + ": " + str('{:.1%} '.format(Candidate_5_p)) + "(" +str(Correy) + ")")
print(Candidate_6 + ": " + str('{:.1%} '.format(Candidate_6_p)) + "(" +str(Li) + ")")
print(Candidate_7 + ": " + str('{:.1%} '.format(Candidate_7_p)) + "(" +str(Otooley) + ")")
print(Candidate_8 + ": " + str('{:.1%} '.format(Candidate_8_p)) + "(" +str(Khan) + ")")
print("----------------")
print("Winner: " + str(Candidate_scores[max(Candidate_p)]))


# write results from election to text file
with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow(["Total Votes: " + str(Total)])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow([Candidate_1 + ": " + str('{:.1%} '.format(Candidate_1_p)) + "(" +str(Cordin) + ")"])
    csvwriter.writerow([Candidate_2 + ": " + str('{:.1%} '.format(Candidate_2_p)) + "(" +str(Vestal) + ")"])
    csvwriter.writerow([Candidate_3 + ": " + str('{:.1%} '.format(Candidate_3_p)) + "(" +str(Torres) + ")"])
    csvwriter.writerow([Candidate_4 + ": " + str('{:.1%} '.format(Candidate_4_p)) + "(" +str(Seth) + ")"])
    csvwriter.writerow([Candidate_5 + ": " + str('{:.1%} '.format(Candidate_5_p)) + "(" +str(Correy) + ")"])
    csvwriter.writerow([Candidate_6 + ": " + str('{:.1%} '.format(Candidate_6_p)) + "(" +str(Li) + ")"])
    csvwriter.writerow([Candidate_7 + ": " + str('{:.1%} '.format(Candidate_7_p)) + "(" +str(Otooley) + ")"])
    csvwriter.writerow([Candidate_8 + ": " + str('{:.1%} '.format(Candidate_8_p)) + "(" +str(Khan) + ")"])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow(["Winner: " + str(Candidate_scores[max(Candidate_p)])])