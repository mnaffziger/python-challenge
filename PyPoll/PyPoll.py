import os
import csv

#find current directory
PyPoll_dir = os.path.dirname(os.path.abspath("PyPoll.py"))

print(PyPoll_dir)
#construct path to csv file
PyPollpath = os.path.join(PyPoll_dir, "python-challenge","PyPoll","Resources","election_data.csv")

with open(PyPollpath,'r') as file:
    reader=csv.reader(PyPoll)
    header=next(header)
    for row in reader:
        print(row)
        