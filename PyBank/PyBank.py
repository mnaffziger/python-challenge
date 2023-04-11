#Dependancies
import os
import csv

#setup file paths
pybank_path=os.path.join(os.getcwd(),'PyBank','Resources','budget_data.csv')

#creates new folder for output if not already in file system
if not os.path.exists(os.path.join("PyBank","Output")): # check to see if dir exists: https://www.tutorialspoint.com/How-can-I-create-a-directory-if-it-does-not-exist-using-Python
    os.mkdir(os.path.join('PyBank','Output'))
pybank_out_path=os.path.join(os.getcwd(),'PyBank','Output','Pybank_calcs.txt')

print(pybank_path)
print(pybank_out_path)

#Initialize variables
months=0
total=0
profit_change=[] 
month_change=[]   
largest_increase=["",0] #Help from class info
largest_decrease=["",9999999999999999999999] #Help from class info  
#change=0

#open original data as read only file
with open(pybank_path,'r') as pybank_in:
    pybank_in=csv.reader(pybank_in, delimiter=",")

    #Generate original header list
    headers=next(pybank_in) 
    tot_header=headers.index('Profit/Losses') #Locates Profit/Losses column index

    first_data=next(pybank_in) #skip headers
    months+=1 #aka row count
    total+=int(first_data[tot_header])
    previous_row=int(first_data[tot_header])
    
    for row in pybank_in:   
        months+=1
        total+=int(row[tot_header])

        #profit changes
        change=int(row[1])-previous_row
        previous_row=int(row[1])
        profit_change+=[change]
        month_change+=[row[0]]

        #find greatest increase
        if change>largest_increase[1]:
                largest_increase[0]=row[0]
                largest_increase[1]=change

        #find greatest decrease
        if change<largest_decrease[1]:
             largest_decrease[0]=row[0]
             largest_decrease[1]=change

ave_change=sum(profit_change)/len(profit_change)

summary =(
        f"Financial Analysis\n"
        f"-------------------------------\n"
        f"Total Months: {months}\n"
        f"Total: ${total}\n"
        f"Average Change: ${ave_change}\n"
        f"Greatest Increase in Profits: {largest_increase[0]} (${largest_increase[1]})\n"
        f"Greastest Decrease in Profits: {largest_decrease[0]} (${largest_decrease[1]})\n"
)

print(summary)

#write txt file
with open(pybank_out_path,"w") as txt_file:
    txt_file.write(summary)

# Be nice!
print(f"A text file containing this summary information has been exported to {pybank_out_path}")    
    
    
    
  