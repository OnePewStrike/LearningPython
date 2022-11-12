import os
import math
from itertools import combinations
from collections import Counter
# Name : Rual Godwin C. Duliente
# Assignment Activity: Association Rule Mining, The Apriori Algorithm


def showMenuOptions():
    print("\nMain Menu")
    print("1. Display data")
    print("2. Display First Iteration")
    print("3. Display Second Iteration")
    print("4. Display Third Iteration")
    print("5. Display All Iterations")
    print("6. Display Candidate Rules")
    print("7. Exit")
    choice = int(input("Enter choice: "))
    return choice


def generateCandidates(data_set):
    candidates = []
    for row in data_set:
        for item in row[1]:
            if item not in candidates:
                candidates.append(item)
    candidates = sorted(candidates)
    return candidates


def inputMinSup(data_set):
    support = float(input(
        "\nPlease enter support threshold (e.g., 0.2, 0.4, 0.9) : "))
    threshold = math.ceil(float(support*len(data_set)))

    return threshold


# def inputMinConf(data_set):
#     confidence = float(input(
#         "\nPlease enter support threshold (e.g., 0.2, 0.4, 0.9) : "))
#     threshold = math.ceil(float(confidence*len(data_set)))

#     return threshold


# Generate First Item Set and Frequent Set
def firstIteration(candidates, data_set, threshold):
    # Filter Candidate Item Sets (C1)
    item_set = Counter()
    for item in candidates:
        for row in data_set:
            if (item in row[1]):
                item_set[item] += 1

    # Filter Frequent Item Sets (L1)
    freq_set = Counter()
    for item in item_set:
        if (item_set[item] >= threshold):
            freq_set[frozenset([item])] += item_set[item]

    return item_set, freq_set


# Generate Second Item Set and Frequent Set
def secondIteration(freq_set, data_set, threshold):
    item_set = set()
    temp = list(freq_set)
    for item in range(0, len(temp)):
        for index in range(item+1, len(temp)):
            item_set.add(temp[item].union(temp[index]))

    # Filter Candidate Item Sets (C2)
    item_set = list(item_set)
    set_two = Counter()
    for item in item_set:
        set_two[item] = 0
        for row in data_set:
            temp = set(row[1])
            if (item.issubset(temp)):
                set_two[item] += 1

    # Filter Frequent Item Sets (L2)
    freq_set = Counter()
    for item in set_two:
        if (set_two[item] >= threshold):
            freq_set[item] += set_two[item]

    return set_two, freq_set


# Generate Third Item Set and Frequent Set
def thirdIteration(freq_set, data_set, threshold):
    item_set = set()
    temp = list(freq_set)
    for item in range(0, len(temp)):
        for index in range(item+1, len(temp)):
            item_set.add(temp[item].union(temp[index]))

    # Filter Candidate Item Sets (C3)
    item_set = list(item_set)
    set_three = Counter()
    for item in item_set:
        set_three[item] = 0
        for row in data_set:
            temp = set(row[1])
            if (item.issubset(temp)):
                set_three[item] += 1

    # Filter Frequent Item Sets (L3)
    freq_set = Counter()
    for item in set_three:
        if (set_three[item] >= threshold):
            freq_set[item] += set_three[item]

    return set_three, freq_set


def displayInitIteration(item_set, freq_set):
    print("\nItemset One (C1) :")
    for item in item_set:
        print('[\'{0}\'] : {1}'.format(item, item_set[item]))

    print("\nFrequent Item Set One (L1): ")
    for item in freq_set:
        print(str(list(item))+": "+str(freq_set[item]))


def displayIteration(item_set, freq_set, num):
    print("\nItemset Two (C{0}) :".format(num))
    for item in item_set:
        print(str(list(item))+": "+str(item_set[item]))

    print("\nFrequent Item Set Two (L{0}): ".format(num))
    for item in freq_set:
        print(str(list(item))+": "+str(freq_set[item]))


def generateCandidateRules(freq_set_three, data_set):
    print("\nCandidate Rules : ")
    for item in freq_set_three:
        rules_set = [frozenset(row) for row in combinations(item, len(item)-1)]
        mmax = 0
        for a in rules_set:
            b = item-a
            ab = item
            sab = 0
            sa = 0
            sb = 0
            print(a)
            input()
            print(b)
            input()
            for row in data_set:
                temp = set(row[1])
                if (a.issubset(temp)):
                    sa += 1
                if (b.issubset(temp)):
                    sb += 1
                if (ab.issubset(temp)):
                    sab += 1
            temp = sab/sa*100
            if (temp > mmax):
                mmax = temp
            temp = sab/sb*100
            if (temp > mmax):
                mmax = temp
            print(str(list(a))+" -> "+str(list(b))+" = "+str(sab/sa*100)+"%")
            print(str(list(b))+" -> "+str(list(a))+" = "+str(sab/sb*100)+"%")


def main():
    threshold = 2
    data_set = [
        ['T100', ['1', '3', '4']],
        ['T200', ['2', '3', '5']],
        ['T300', ['1', '2', '3', '5']],
        ['T400', ['2', '5']]
    ]

    threshold = inputMinSup(data_set)
    candidates = generateCandidates(data_set)
    item_set_one, freq_set_one = firstIteration(
        candidates, data_set, threshold)
    item_set_two, freq_set_two = secondIteration(
        freq_set_one, data_set, threshold)
    item_set_three, freq_set_three = thirdIteration(
        freq_set_two, data_set, threshold)

    while True:
        os.system("cls")
        choice = showMenuOptions()
        if (choice == 1):
            print(data_set)
            input("\n\nEnter to continue")
            continue
        elif (choice == 2):
            displayInitIteration(item_set_one, freq_set_one)
            input("\n\nEnter to continue")
            continue
        elif (choice == 3):
            displayIteration(item_set_two, freq_set_two, 2)
            input("\n\nEnter to continue")
            continue
        elif (choice == 4):
            displayIteration(item_set_three, freq_set_three, 3)
            input("\n\nEnter to continue")
            continue
        elif (choice == 5):
            displayInitIteration(item_set_one, freq_set_one)
            displayIteration(item_set_two, freq_set_two, 2)
            displayIteration(item_set_three, freq_set_three, 3)
            input("\n\nEnter to continue")
            continue
        elif (choice == 6):
            generateCandidateRules(freq_set_three, data_set)
            input("\n\nEnter to continue")
            continue
        elif (choice == 7):

            break
        else:
            print("\nError : the choice does not exist, please try again...")
            continue
    print("\nEnd of program")


main()
