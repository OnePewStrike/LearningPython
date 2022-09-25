import csv
import pandas as pd


def viewOriginalData():
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            print(line)


def solveByRemoveRows():
    L = []
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            if row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '':
                continue
            else:
                L.append(row)

        with open("new_data_format.csv", 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerows(L)


def solveByAverage():
    L = []
    average = 0.0
    count = 0
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        for row in csv_reader:
            average += float(row[0])
            count += 1
        average = average / count

        for row in csv_reader:
            if row[0] == '':
                L.append(average)
            else:
                L.append(row)

        with open("new_data_format.csv", 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerows(L)


solveByAverage()
