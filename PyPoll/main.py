
#Calculate candidate totals and percentages from election data then push to git hub repo
#import and read the csv file for election_data
f = open('PyPoll.txt','w')
import os
import csv
csvpath = os.path.join("election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)


#total number of votes cast using counter
#use loop to obtain name with the percentage and total number of votes per candidate
#print results
#identify a winner, print

    counter = 0
    myDict = {}
    row_number = 0
    next(csvreader)
    for row in csvreader:
        counter= counter + 1

        row_number +=1
        if row[2] in myDict:
            myDict[row[2]] += 1
        else:
            myDict[row[2]] = 1

    print("Election Results", file=open("PyPoll.txt", "a") )
    print("Total Votes: ", counter, file=open("PyPoll.txt", "a"))
    
    for name in myDict:
        votebycan = (myDict[name])
        fraction = (myDict[name])/row_number
        percentage = 100*fraction



        print(name, ""+"{:.2%}".format(fraction), votebycan, file=open("PyPoll.txt", "a"))
    

    #print(myDict)
    #Identify the winner using the dictionary created above- tricky for when we need the max based 
    #max but the corresponding name needs to be printed

    max_value = max(myDict.values()) 
    #max keys identifies the corresponding name
    max_keys = [i for i, v in myDict.items() if v == max_value]

    print("Winner: ", max_keys, file=open("PyPoll.txt", "a"))
    f.close()

    #Program Complete
    

        







