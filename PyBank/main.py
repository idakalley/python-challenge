import os

# Module for reading CSV files
import csv
import datetime

csvpath = os.path.join('..','python-challenge','PyBank','Resources','budget_data.csv')


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    profit= []
    monthly_changes= []
    date= []

# Variables used
    count= 0
    total_profit= 0
    total_change_profits= 0
    initial_profit= 0
    

    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header= next(csvreader)

    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

    # Date is required for greatest increase and decrease in profits
        date.append(row[0])

    # Total number of votes 
        count= count + 1

    # The net total amount of "Profit/Losses" over the entire period
    # Append the profit information and calc total profit
        profit.append(row[1])
        total_profit= total_profit + int(row[1])

        
    # Find change in profits between begin month and at end month
        final_profit= int(row[1])
        monthly_change_profits= final_profit - initial_profit

    # Store monthly_changes_profits in a list using append
        monthly_changes.append(monthly_change_profits)

        total_change_profits= total_change_profits + monthly_change_profits
        initial_profit= final_profit

    # Calc the average change in profit
        average_change_profits= (total_change_profits/count-1)
        greatest_increase_profits = max(monthly_changes)
        greatest_decrease_profits = min(monthly_changes)

        increase_date = date[monthly_changes.index(greatest_decrease_profits)]
        decrease_date = date[monthly_changes.index(greatest_increase_profits)]



    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("Average Change: " + "$" + str(int(average_change_profits)))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_decrease_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_increase_profits)+ ")")
    print("----------------------------------------------------------")

output_file = os.path.join('PyBank', 'analysis', 'financial_analysis.txt')
with open(output_file, "w", newline="") as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")
