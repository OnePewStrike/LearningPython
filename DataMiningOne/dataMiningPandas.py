import csv
import pandas as pd

df = pd.read_csv("data.csv")
df


def viewOriginalData():
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            print(row)
