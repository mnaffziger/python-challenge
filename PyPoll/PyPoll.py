#Dependancies
import os
import csv

#setup file paths
pypoll_path=os.path.join(os.getcwd(),'PyPoll','Resources','election_data.csv')

#creates new folder for output if not already in file system
if not os.path.exists(os.path.join("PyPoll","Output")): # check to see if dir exists: https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
    os.mkdir(os.path.join('PyPoll','Output'))
pypoll_out_path=os.path.join(os.getcwd(),'PyPoll','Output','PyPoll_calcs.txt')

#setup/initialize counters, setup lists and dictionaries
total_votes=0
highest_votes=0
ballot_candidates=[]
candidate_tally={}
winner=""
working= "."

#read original election results csv and extract unique candidates
with open(pypoll_path,'r') as ballot_votes:
    ballot_votes=csv.reader(ballot_votes,delimiter=",")
    
    headers=next(ballot_votes) #skip headers

    for row in ballot_votes:
        
        print(working, end = ''), #this is cool- got it from class help/solutions
        
        #tally unique votes for each candidate
        total_votes=total_votes +1
        candidate=row[2]

        #got a lot of help on this one to utilize the loop to add strings as the data is read row by row
        if candidate not in ballot_candidates:
            ballot_candidates.append(candidate)
            candidate_tally[candidate]=0
        candidate_tally[candidate]=candidate_tally[candidate]+1

#Generate txt file format
with open(pypoll_out_path,'w') as txt_file:
    results =(
        f"\n \nElection Results\n"
        f"-----------------------------------------\n"
        f"\n"
        f"Total Votes: {total_votes}\n"
        f"\n"
        f"-----------------------------------------\n"
        f"\n"
        )
    print(results,end="")
    txt_file.write(results)

    #generate voting results template for txt file
    for person in candidate_tally:
        
        votes = candidate_tally.get(person)
        vote_percent=float(votes)/(float(total_votes))*100

        #determine winner
        if (votes>highest_votes):
            highest_votes = votes
            winner = person
    
        #Report votes and winner to terminal window
        ballot_candidate_votes=f"{person}: {vote_percent:.3f}% ({votes})\n"
        print(ballot_candidate_votes,end="")
        txt_file.write(ballot_candidate_votes)
         
    #Print election winner
    election_winner_result=(
        f"\n"
        f"-----------------------------------------\n"
        f"\n"
        f"Winner: {winner}\n"
        f"\n"
        f"-----------------------------------------\n"
        )
    print(election_winner_result)

    #save to txt file
    txt_file.write(election_winner_result)

# Be nice!
be_nice=(
    f"\nA text file containing these election results has been exported to:\n"
    f"\n"
    f"{pypoll_out_path}\n"
    )
print(be_nice)
