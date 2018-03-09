import os
import csv

# Path to collect data from the Resources folder
wrestlingCSV = os.path.join('Resources','WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def getPercentages(wrestlerData):
    
    # Total matches can be found by adding wins, losses, and draws together
    totalMatches = int(wrestlerData[1]) + int(wrestlerData[2]) + int(wrestlerData[3])

    # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    winPercent = (int(wrestlerData[1])/totalMatches)*100

    # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    lossPercent = (int(wrestlerData[2])/totalMatches)*100

    # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    drawPercent = (int(wrestlerData[3])/totalMatches)*100

    # If the loss percentage is over 50, typeOfWrestler is "Jobber". Otherwise it is "Superstar".
    if(lossPercent > 50):
        typeOfWrestler = "Jobber"
    else:
        typeOfWrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    print("Stats for " + wrestlerData[0])
    print("WIN PERCENT: " + str(winPercent))
    print("LOSS PERCENT: " + str(lossPercent))
    print("DRAW PERCENT: " + str(drawPercent))
    print(wrestlerData[0] + " is a " + typeOfWrestler)

# Read in the CSV file
with open(wrestlingCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    nameToCheck = input("What wrestler do you want to look for? ")
    
    # Loop through the data
    for row in csvreader:
        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(nameToCheck == row[0]):
            getPercentages(row)








# Initial variable to track shopping status
shopping = 'y'

# List to track pie purchases
pie_purchases = [0,0,0,0,0,0,0,0,0,0]

# Pie List 
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", 
            "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# Display initial message
print("Welcome to the House of Pies! Here are our pies:")

# While we are still shopping...
while shopping == "y":

  # Show pie selection prompt 
  print("---------------------------------------------------------------------")
  print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, " +
        " (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
        " (9) Tamale, (10) Steak ")

  pie_choice = input("Which would you like? ")

  # Add pie to the pie list by finding the matching index and adding one to its value
  pie_purchases[int(pie_choice)-1] = pie_purchases[int(pie_choice)-1] + 1

  print("------------------------------------------------------------------------")

  # Inform the customer of the pie purchase
  print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")

  # Provide exit option
  shopping = input("Would you like to make another purchase: (y)es or (n)o? ")

# Once the pie list is complete 
print("------------------------------------------------------------------------")

# Count instances of each pie
print("You purchased: ")

# Loop through the full pie list
for pie_index in range(len(pie_list)):

  # Gather the count of each pie in the pie list and print them alongside the pies
  print(str(pie_purchases[pie_index]) + " " + str(pie_list[pie_index]))

