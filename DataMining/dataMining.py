import csv

with open("data.csv", "r") as infile:
    reader = csv.reader(infile, delimiter=",")
    header = next(reader)
    print(header)
