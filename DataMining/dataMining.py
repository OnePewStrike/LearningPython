import csv


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
    total = None
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            header = next(csv_reader)
            total = int(row[0])
        print("\n\tThe total is {}", total)

        for row in csv_reader:
            if row[0] == '':
                continue
            else:
                L.append(row)

        with open("new_data_format.csv", 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerows(L)


solveByRemoveRows()
