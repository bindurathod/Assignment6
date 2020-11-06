import csv

with open('players.csv', 'rt') as f:
    csv_reader = csv.reader(f)

    for line in csv_reader:
        print(line)
