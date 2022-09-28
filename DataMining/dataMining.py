# Name: Rual Godwin C. Duliente
# Subject: Data Mining
import csv


def viewOriginalData():
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            print(row)


def viewFormattedData():
    with open('new_data_format.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            print(row)


def solveByRemoveRows():
    L = []
    isFound = False
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            for index in range(0, 5):
                if row[index] == '':
                    isFound = True
            if not isFound:
                L.append(row)
            isFound = False

        with open("new_data_format.csv", 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerows(L)


def solveByAverage():
    L = []

    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            for index in range(0, 5):
                if row[index] == '':
                    row[index] = str(getAverage(index))
            L.append(row)

        with open("new_data_format.csv", 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerows(L)


def getAverage(index):
    average = 0.0
    total = 0.0
    count = 0
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        for row in csv_reader:
            if (row[index] == ''):
                continue
            average += float(row[index])
            count += 1
        total = average / count
        total_convert = "{:.2f}".format(total)
    return str(total_convert)


def solveByGlobalConstant():
    L = []
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            for index in range(0, 5):
                if row[index] == '':
                    row[index] = '0'
            L.append(row)

        for row in csv_reader:
            print(row[0])

        with open("new_data_format.csv", 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerows(L)


def solveByLinearInterpolation():
    L = []
    isFound = False
    position = 1

    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            for index in range(0, 5):
                if row[index] == '':
                    target_row = row
                    L.append(solveTargetIndex(
                        index, prev_row, target_row, position))
                    isFound = True
            if isFound:
                isFound = False
                position += 1
                continue
            L.append(row)
            prev_row = row
            position += 1

        with open("new_data_format.csv", 'w') as new_file:
            csv_writer = csv.writer(new_file, delimiter=",")
            csv_writer.writerows(L)


def solveTargetIndex(index, prev_row, target_row, position):
    initial = 0
    prev = 0.0
    after = 0.0
    mean = 0.0
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        for row in csv_reader:
            if (position != initial):
                initial += 1
                continue
            else:
                after = float(row[index])
                prev = float(prev_row[index])
                mean = (after + prev) / 2
                format_mean = "{:.2f}".format(mean)
                target_row[index] = format_mean
                temp = target_row
                return temp


def showMenuOptions():
    print("\nMain Menu")
    print("1. Show original data")
    print("2. Show formatted data")
    print("3. Solve by removing rows with missing data")
    print("4. Solve by average")
    print("5. Solve by linear interpolation")
    print("6. Solve by global constant")
    print("7. Exit")
    x = int(input("User choice: "))
    return x


while True:
    choice = int(showMenuOptions())
    if (choice == 1):
        viewOriginalData()
        input("Enter to continue..")
        continue
    elif (choice == 2):
        viewFormattedData()
        input("Enter to continue..")
        continue
    elif (choice == 3):
        solveByRemoveRows()
        input("Enter to continue..")
        continue
    elif (choice == 4):
        solveByAverage()
        input("Enter to continue..")
        continue
    elif (choice == 5):
        solveByLinearInterpolation()
        input("Enter to continue..")
        continue
    elif (choice == 6):
        solveByGlobalConstant()
        input("Enter to continue..")
        continue
    elif (choice == 7):
        break
    else:
        print("\tError: choice does not exist... Try again")
        continue
print("\tEnd of program")

# with open('data.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)

#      next(csv_reader)
#       for row in csv_reader:
#            for index in range(0, 4):
#                 if row[index] == '':
#                     target_row = row
#                     temp.append(solveTargetIndex(
#                         index, prev_row, target_row, position))
#                     isFound = True
#                     continue
#                 else:
#                     temp.append(row[index])
#                     print("CHECK TEMP: ", temp)
#             if isFound:
#                 temp = []
#                 L.append(temp)
#                 isFound = False
#                 position += 1
#                 continue
#             else:
#                 L.append(row)
#                 prev_row = row
#                 position += 1
