def newDataEntry():
    data = []

    data = list(map(int, input("Enter the list of data : ").split()))
    return data


def displayData(data):
    print(data)
    return


def binByWidth(data, k):
    length = len(data)
    w = int((max(data)-min(data))/k)
    minData = min(data)
    arr = []
    for i in range(0, k + 1):
        arr = arr + [minData + w * i]
    arri = []

    for i in range(0, k):
        temp = []
        for j in data:
            if j >= arr[i] and j <= arr[i+1]:
                temp += [j]
        arri += [temp]
    print(arri)


def binByFrequency(data, k):
    length = len(data)
    size = int(length / k)

    for i in range(0, k):
        arr = []
        for j in range(i * size, (i + 1) * size):
            if j >= length:
                break
            arr = arr + [data[j]]
        print(arr)


def showMenuOptions():
    print("\nMain Menu")
    print("1. Enter data")
    print("2. Display data")
    print("3. Bin data using width")
    print("4. Bin data using frequency")
    print("5. Exit")
    choice = int(input("Enter choice: "))
    return choice


data = [13, 15, 16, 16, 17, 19, 20, 21, 22, 25, 30, 33, 35, 36, 40]
while True:
    choice = showMenuOptions()
    if (choice == 1):
        data = newDataEntry()
        continue
    elif (choice == 2):
        displayData(data)
        continue
    elif (choice == 3):
        k = int(input("Enter the bin width : "))
        binByWidth(data, k)
        continue
    elif (choice == 4):
        k = int(input("Enter the bin width : "))
        binByFrequency(data, k)
        continue
    elif (choice == 5):
        break
    else:
        print("\nError: The choice does not exist... try again.")
        continue
print("End of program")
