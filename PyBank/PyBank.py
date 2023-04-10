import os
import csv

# Create variable for file path
pybank_path=os.getcwd()

#open and initial csv analysis taken from class notes/solved problems
with open(pybank_path) as pybank_csv:
    pybank_csv=csv.reader(pybank_csv, delimiter=",")
    pybank_header=next(pybank_csv) #skip headers
    
    months=sum(1 for row in pybank_csv)

