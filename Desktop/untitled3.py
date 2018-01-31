import csv
import sys

genename = raw_input('Enter a gene name')

csv_file = csv.reader(open('Exercise.csv', "rb"), delimiter=",")

for row in csv_file:
  if genename == row[3]:
	 print(row)
	 
 
print("the gene "+genename+" has a total of ",sum(1 for row in genename),
"mutations listed.The OMIM id is",['OMIM Gene Id']) 
       
csv_file = csv.writer(open('Exercise.csv', "w"), delimiter=",")
data=[['Chromosome','start pos','end pos',REF,ALT]]    
with myFile:  
   writer = csv.writer(csv_file)
   writer.writerows(data)
