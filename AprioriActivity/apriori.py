import csv
import itertools

supDict = {}


def showMenuOptions():
    print("\nMain Menu")
    print("1. Display data")
    print("2. Solve by Apriori")
    print("3. Exit")
    choice = int(input("Enter choice: "))
    return choice


def inputMinSup():
    sup = input("Please enter sup threshold : ")
    return int(sup)


def inputMinConf():
    conf = input("Please enter confidence threshold : ")
    return int(conf)


def viewOriginalData():
    with open('apriori_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        for row in csv_reader:
            print(row)


def load_data(path):
    transactions = []
    with open(path) as f:
        dataset = f.readlines()

    for line in dataset:
        transactions.append(sorted(line.strip().split(",")))

    return transactions


def generateF1(dataset, minSupport, T):

    prodDict = {}
    returnSet = []

    for data in dataset:
        for prod in data:
            if prod not in prodDict:
                prodDict[prod] = 1
            else:
                prodDict[prod] += 1

    for key in prodDict:
        temp = []
        sup = prodDict[key]/T
        if sup >= minSupport:
            temp.append(key)
            returnSet.append(temp)
            supDict[tuple(temp)] = prodDict[key]

    return (returnSet)


def main():
    data = "groceries.csv"
    transactions = load_data(data)

    sizeOfTransactions = len(transactions)
    minSup = inputMinSup()
    minConf = inputMinConf()

    F1 = generateF1(transactions, minSup, sizeOfTransactions)
    print(F1)

    # while True:
    #     choice = showMenuOptions()
    #     if (choice == 1):
    #         viewOriginalData()
    #         continue
    #     elif (choice == 2):
    #         minSup = inputMinSup()
    #         minConf = inputMinConf()
    #         continue
    #     elif (choice == 3):
    #         break
    #     else:
    #         print("\nError : the choice does not exist, please try again...")
    #         continue
    # print("\nEnd of program")


main()
