import os

# Module for reading CSV files
import csv


csvpath = os.path.join('..','python-challenge','PyPoll','Resources','election_data.csv')
# variables
total_votes = 0
# Initialise list of unique candidates
candidates_unique = []

candidate_vote_count = []


# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
  
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Machine read object
    # print(csvreader)

    # Read the header row first (skip this step if not required header)
    csv_header= next(csvreader)

    # optional print header of election_data.csv
    #print(f"CSV Header: {csv_header}")
   
    #The total number of votes cast
    # total_votes=lines=len(list(csvreader))

    #A complete list of candidates who received votes (get list of unique candidates from the set)
    for row in csvreader:
    # This is the total votes cast, just count rows
        total_votes += 1
    # read in the candidate from column 3 of csv
        candidate_in = (row[2])
    # if candidate already in list then locate the candidate by index # (sets have no index/could not use set()) and increment the vote count by 1
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
    # if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)


    # print(f'Total votes {total_votes}')
    # print(f'Each candidate: {candidates_unique}')
    # print(f'Index: {candidates_unique.index(candidate_in)}')

    # Initialise list
    pct = []
    max_votes = candidate_vote_count[0]
    max_index = 0


for x in range(len(candidates_unique)):
    # calculation to get the percentage of votes each unique candidate received
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index]


#QA the variables
# print(f'Vote count for each candidate: {candidate_vote_count}')
# print(f'Max votes: {max_votes}')
# print(f'Election winner: {election_winner}')

print('======================================================')
print('|                  Election Results                  |')
print('======================================================')
print(f'Total Votes: {total_votes}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Election winner: {election_winner.upper()}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')




#output txt file
output_file = os.path.join('PyPoll', 'analysis', 'pypoll_created_with.txt')
with open(output_file, "w", newline="") as datafile:
    datafile.write('======================================================\n')
    datafile.write('|                  Election Results                  |\n')
    datafile.write('======================================================\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write("---END OF REPORT---")


        

    

 
