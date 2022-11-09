import math


def inputData():
    data = []

    data = list(map(int, input("Enter the list of data : ").split()))
    return data


def displayData(data):
    print(data)
    return


def displayResult(res):
    print(res)
    return


def newDataEntry():
    data = []

    data = list(map(int, input("Enter the list of data : ").split()))
    return data


def displayData(data):
    print(data)
    return


def displayResult(res):
    print(res)
    return


def binByWidth(data, k):
    w = math.ceil(float((max(data)-min(data))/k))

    binIndex = []
    for i in range(0, k+1):
        binIndex.append([min(data) + w * i])

    binResult = []
    for i in range(0, k):
        temp = []
        for j in data:
            if j >= binIndex[i] and j <= binIndex[i+1]:
                temp.append(j)
        binResult.append[temp]
    return binResult


def binByFrequency(data, k):
    length = len(data)
    binSize = math.ceil(float(length/k))
    pos = 0

    binResult = []
    for i in range(0, k):
        temp = []
        for j in range(0, binSize):
            if j >= length:
                break
            elif pos >= length:
                break
            else:
                temp.append(data[pos])
                pos += 1
        binResult += [temp]
    return binResult


def showMenuOptions():
    print("\nMain Menu")
    print("1. Enter data")
    print("2. Display data")
    print("3. Display result")
    print("4. Bin data using width")
    print("5. Bin data using frequency")
    print("6. Exit")
    choice = int(input("Enter choice: "))
    return choice


def showMenuOptions():
    print("\nMain Menu")
    print("1. Enter new data")
    print("2. Display data")
    print("3. Display result")
    print("4. Bin data using width")
    print("5. Bin data using frequency")
    print("6. Bin smooth data by means")
    print("7. Bin smooth data by boundary")
    print("8. Exit")
    choice = int(input("Enter choice : "))
    return choice


data = [13, 15, 16, 16, 17, 19, 20, 21, 22, 25, 30, 33, 35, 36, 40]
result = []

data = [3, 7, 8, 13, 22, 22, 22, 26, 26, 28, 30, 37]
k = 3
binResult = []

while True:
    choice = showMenuOptions()
    if (choice == 1):
        data = inputData()
        continue
    elif (choice == 2):
        displayData(data)
        continue
    elif (choice == 3):
        displayResult(binResult)
    elif (choice == 4):
        k = inputWidth()
        binResult = binByWidth(data, k)
        continue
    elif (choice == 5):
        k = inputWidth()
        binResult = binByFrequency(data, k)
        continue
    elif (choice == 6):
        k = inputWidth()
        binResult = binByMeans(data, k)
        continue
    elif (choice == 7):
        k = inputWidth()
        binResult = binByBoundary(data, k)
        continue
    elif (choice == 8):
        break
    else:
        print("\nError: The choice does not exist... try again.")
        continue
print("End of program")
