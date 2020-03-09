# csv 
import csv

with open('csv.csv', 'r') as obj:
    obj = csv.reader(obj)

    sum = 0
    for i, row in enumerate(obj):
        print(i, row[0], row[1])
        sum += int(row[1]) if i > 0 else 0
        print("Total CostL ", sum)  