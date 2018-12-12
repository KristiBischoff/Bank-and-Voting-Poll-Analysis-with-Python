#import and read the csv file for budget_data
f = open('PyBank.txt','w')
import os
import csv
csvpath = os.path.join("budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #set variables equal to 0
    counter=0
    Net_profit_loss=0
    Profit_diff=[ ]

    next(csvreader)
    #create a for loop that identifies the first row and sets it to 0, due to the difference not being calculated
    #When the the iteration is at the second row, then the difference between the current and the previous row is calculated
    #for profit/losses

    firstrow=True
    for row in csvreader:
        #calculate number of months
        counter=counter+1
        if firstrow == True:
            firstrow=False
            prev_mon_profit = int(row[1])
        curr_mon_profit = int(row[1])
        #append the difference between profit/loss to the list created above
        Profit_diff.append(curr_mon_profit - prev_mon_profit)

        #each iteration will lead to the previous value becoming the current- need to assign here
        prev_mon_profit = curr_mon_profit

        #Calculate the Net Profit/Loss 
        Net_profit_loss= Net_profit_loss + int(row[1])

    #calculate the average of the monthly differences in profit loss
    
    #Since 0 is the starting value, we want to treat this as not the total row differences calculated
    #The total number of rows is 86, but we have 85 profit/loss differences calculated so that should be the
    #denominator. Need to subtract 1 from the number of rows.

    #new denominator
    denom = len(Profit_diff) - 1
    #print(denom)

    #calculate average difference in profit loss using new denominator variable
    def Average(Profit_diff):
        return sum(Profit_diff) / denom
    Average_diff = Average(Profit_diff) 

    #Identify greatest increase in profit/loss

    def Maximum(Profit_diff):
        return ((row[0]), max(Profit_diff))
    Maximum_incr = Maximum(Profit_diff)


        #Identify greatest decrease in profit/loss
    def Minimum(Profit_diff):
        return (str(row[0]), min(Profit_diff))
    Minimum_decr = Minimum(Profit_diff)
    
    
    #print results
    print("Results", file=open("PyBank.txt", "a"))
    print("Total Months: ", counter, file=open("PyBank.txt", "a"))
    print("Total: ", Net_profit_loss, file=open("PyBank.txt", "a"))
    #print(Profit_diff, file=open("PyBank.txt", "a"))
    print("Average Change: ", Average_diff, file=open("PyBank.txt", "a"))
    print("Greatest Increase in Profits: ", Maximum_incr, file=open("PyBank.txt", "a"))
    print("Greatest Decrease in Profits: ", Minimum_decr, file=open("PyBank.txt", "a"))
f.close()

#Program Complete


