import csv
filename = input("Enter the CSV file name (with .csv extension): ")
colread = input("Enter column indices to read (comma-separated, starting from 0): ")
colread = [int(x.strip()) for x in colread.split(",")] # Convert the input to a list of integers
with open(filename, 'r') as csvfile1:
    csvreader = csv.reader(csvfile1)
    for row in csvreader: # Iterate through each row
        selectcol = [row[col] for col in colread if col < len(row)]
        print(selectcol)