### TASK 3 ###

# Import CSV
import csv
# Import the datetime module and shorten the name to dt
from datetime import datetime as dt
# Create empty list
list=[]

# Load csv file and shapeshift
file = open('shapeshift.csv','r')
# Reads the file in a dictionary format
reader = csv.DictReader(file)

# For loop to iterate through the timestamp row
for row in reader:
    date = dt.fromtimestamp(float(row['timestamp']))
    row['timestamp'] = date
    # Adds the timestamp data into the empty list
    list.append(row)

# Sorts the timestamp data
list.sort(key = lambda x : x['timestamp'])

print list
