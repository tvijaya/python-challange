import os
import csv

voterIds = []
candidates = []
with open('election_data_2.csv', newline = '') as electionOne:
    csvreader = csv.reader(electionOne, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        voterIds.append(row[0])
        candidates.append(row[2])

unique_candidates = list(set(candidates))

voting = zip(voterIds, candidates)

candidateVotes = dict()

for candidate in unique_candidates:
    candidateVotes[candidate] = 0

for vote, candidate in voting:
    if(candidate in candidateVotes):
        candidateVotes[candidate] +=  1


sortedValues  = sorted(candidateVotes.values(), reverse=True)
totalVotes = len(voterIds)
print("Election Results")
print("_________________")
print("Total Votes: " + str(totalVotes))
print("_________________")
for key, value in candidateVotes.items():
    print(key + ": " + str(round(((value/totalVotes)*100),2)) + "%  (" + str(value) + ")")
print("_________________")
for key, value in candidateVotes.items():
    if (value == sortedValues[0]) :
        print("Winner : " + key)
print("_________________")



with open("Election_Results2.txt", 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("_________________\n")
    text_file.write("Total Votes: " + str(totalVotes) + "\n")
    text_file.write("_________________\n")
    for key, value in candidateVotes.items():
        text_file.write(key + ": " + str(round(((value/totalVotes)*100),2)) + "%  (" + str(value) + ")\n")
    text_file.write("_________________\n")
    for key, value in candidateVotes.items():
        if (value == sortedValues[0]) :
            text_file.write("Winner : " + key + "\n")
    text_file.write("_________________\n")
    