import csv

# CREATE_ROW: used to create dict-style row for spreadsheet
# input:    columns (as list)
# output:   row (as dict)
def create_row(columns):
    # columns are: (0) start date,
    #              (1) start time,
    #              (2) end date,
    #              (3) end time,
    #              (4) free text
    d = {'start date' : columns[0], 'start time' : columns[1],
         'end date' : columns[2], 'end time' : columns[3],
         'text' : columns[4]}
    return d

#prefix = '../../data/'

f = open('church_metal_theft.csv', 'r')
r = csv.DictReader(f, delimiter='|')

# read in contents of file, line by line

spreadsheet = []

for row in r:
    spreadsheet.append(row)
print spreadsheet