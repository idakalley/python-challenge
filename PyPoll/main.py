import os

# Module for reading CSV files
import csv


csvpath = os.path.join('..','python-challenge','PyPoll','Resources','election_data.csv')


# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    new_candidate_list= set()
    vote_list= []
    max_votes_count= each_candidate_count= 0
    max_location= 0

    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #Machine read
    #print(csvreader)

    # Read the header row first (skip this step if there is no header)
    csv_header= next(csvreader)

    #print(f"CSV Header: {csv_header}")
   
    #The total number of votes cast
    # lines=len(list(csvreader))

    #A complete list of candidates who received votes
    
    for row in csvreader:
        new_candidate_list.add (row[2])

    print (new_candidate_list)

    # The percentage of votes each candidate won

    for x in range(len(new_candidate_list)):   
    #calculation to get the percentage, x is the looper value
        voter_cand = round(new_candidate_list[x]/total_votes*100, 2)
        pct.append(voter_cand)
    
    if candidate_vote_count[x] > max_votes:
        max_votes_count = each_candidate_count[x]
        max_location = x

election_winner = new_candidate_list[max_location] 




    # The total number of votes each candidate won

    # The winner of the election based on popular vote.
        

    # print(lines)
    print(new_candidate_list)

 
