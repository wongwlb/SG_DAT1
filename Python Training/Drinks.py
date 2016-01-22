# import drinks csv
import csv
with open('C:\Users\Brandon\SG_DAT1\data\drinks.csv', 'rU') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
     for row in spamreader:
         print ', '.join(row)

f.read()
f.close()
