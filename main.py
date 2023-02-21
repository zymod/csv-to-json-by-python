import csv
import json


with open('employees.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)
    header = [col.replace(' ', '') for col in next(csv_reader)]
    rows = [dict(zip(header, row)) for row in csv_reader] # $

with open('employees.json', 'w') as file:
    json.dump(rows, file, separators=(',', ':'), indent=4)
