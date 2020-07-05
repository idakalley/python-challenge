import os

# Module for reading CSV files
import csv

csvpath = os.path.join('..','python-challenge','PyBank','Resources','budget_data.csv')


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    count_total= 0
    sum_total= 0
    average_change= 0
    change_list = []
    averageSum= 0
    date_list= []
    datemax=0
    datemin=0

    


    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header= next(csvreader)

    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        count_total= count_total+1

        sum_total= sum_total + int(row[1])

        Profit_Losses= int(row[1])
        change_calc= Profit_Losses - average_change
        change_list.append(change_calc)
        
        average_change= Profit_Losses
        date_list.append(row[0])

        
        
    #print(row)
    print(count_total)
    print(sum_total)
    change_list.pop(0)
    print(change_list)
    averageSum= round(sum(change_list)/(count_total-1),2)
    print(averageSum)
    print(max(change_list))
    print(min(change_list))
    date_list.pop(0)
    datemax= change_list.index(max(change_list))
    print(date_list[datemax])
    datemin= change_list.index(min(change_list))
    print(date_list[datemin])

    
