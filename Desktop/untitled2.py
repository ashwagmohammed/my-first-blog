import csv
with open('Exercise.csv', 'r') as f:
    d_reader = csv.DictReader(f)
ifile = open('Exercise.csv', "rb")
reader = csv.reader(ifile)
 
genename=input("Enter gene name")
   
        print(headers)
