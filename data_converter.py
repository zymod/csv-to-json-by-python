import csv
import json

csv_file = 'employees.csv'  # nazwa pliku csv
json_file = 'employees.json'  # nazwa pliku json

# otwórz plik csv i przeczytaj jego zawartość
with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# zapisz dane z pliku csv do pliku json
with open(json_file, 'w') as f:
    json.dump(rows, f, indent=4)