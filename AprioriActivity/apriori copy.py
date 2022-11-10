import csv
from collections import defaultdict


def showMenuOptions():
    print("\nMain Menu")
    print("1. Display data")
    print("2. Display item count")
    print("3. Display Frequent Itemset One")
    print("4. Display Frequent Itemset Two")
    print("5. Display Frequent Itemset Three")
    print("6. Display Candidate Rules")
    print("7. Exit")
    choice = int(input("Enter choice: "))
    return choice


def inputMinSup():
    sup = input("\nPlease enter sup threshold (e.g., 50) : ")
    return int(sup)


def inputMinConf():
    conf = input("\nPlease enter confidence threshold (e.g., 50) : ")
    return int(conf)


def viewOriginalData():
    with open('groceries.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        next(csv_reader)
        for row in csv_reader:
            print(row)


def readData():
    with open("groceries.csv") as f:
        data = f.readlines()
    f.close()

    return data


def displayItemCount(data):
    item_counts = defaultdict(int)

    for x in data:
        for item in x.split():
            item_counts[item] += 1

    print(item_counts)


# Sort pair sets such as (a,b) is the same as (b,a)
def sort_group(*args):
    return str(sorted(args))


def generate_pairs(*args):
    pairs = []
    for set_one in range(len(args) - 1):
        for set_two in range(set_one + 1, len(args)):
            pairs.append(sort_group(args[set_one], args[set_two]))
    return pairs


# Filter for Frequent Item Set One
def firstIteration(data, threshold):
    item_counts = defaultdict(int)

    for x in data:
        for item in x.split():
            item_counts[item] += 1

    return item_counts


# Filter for Frequent Item Set Two
def secondIteration(data, threshold):
    pair_counts = defaultdict(int)
    item_counts = firstIteration(data, threshold)

    frequent_items = set()
    for key in item_counts:
        if item_counts[key] > threshold:
            frequent_items.add(key)

    for x in data:
        items = x.split()
        for set_one in range(len(items) - 1):
            if items[set_one] not in frequent_items:
                continue
            for set_two in range(set_one + 1, len(items)):
                if items[set_two] not in frequent_items:
                    continue
                # sort (a,b) is the same as (b, a)
                pair = sort_group(items[set_one], items[set_two])
                pair_counts[pair] += 1

    return pair_counts

    frequent_pairs = set()
    for key in pair_counts:
        if pair_counts[key] > threshold:
            frequent_pairs.add(key)
    return frequent_pairs


# Filter for Frequent Item Set Three
def thirdIteration(data, threshold):
    triple_counts = defaultdict(int)
    item_counts = firstIteration(data, threshold)
    pair_counts = secondIteration(data, threshold)

    frequent_items = set()
    for key in item_counts:
        if item_counts[key] > threshold:
            frequent_items.add(key)

    frequent_pairs = set()
    for key in pair_counts:
        if pair_counts[key] > threshold:
            frequent_pairs.add(key)

    for x in data:
        items = x.split()
        for set_one in range(len(items) - 1):
            if items[set_one] not in frequent_items:
                continue
            for set_two in range(set_one + 1, len(items)):
                if items[set_two] not in frequent_items:
                    continue
                first_pair = sort_group(items[set_one], items[set_two])
                if first_pair not in frequent_pairs:
                    continue
                for set_three in range(set_two + 1, len(items)):
                    if items[set_three] not in frequent_items:
                        continue
                    pairs = generate_pairs(
                        items[set_one], items[set_two], items[set_three])
                    if any(pair not in frequent_pairs for pair in pairs):
                        continue
                    triple = sort_group(
                        items[set_one], items[set_two], items[set_three])
                    triple_counts[triple] += 1

    # frequent_triples = set()
    # for key in triple_counts:
    #     if triple_counts[key] > threshold:
    #         frequent_triples.add(key)

    return triple_counts
    for key, value in sorted(triple_counts.items()):
        if value > threshold:
            print(key, value)

    return


def displayItemSet(item_count, threshold):
    for key, value in sorted(item_count.items()):
        if value > threshold:
            print(key, value)


def main():
    data = readData()
    freqItemSet = set()

    while True:
        choice = showMenuOptions()
        if (choice == 1):
            viewOriginalData()
            continue
        elif (choice == 2):
            displayItemCount(data)
            continue
        elif (choice == 3):
            minConf = inputMinConf()
            freqItemSet = firstIteration(data, minConf)
            displayItemSet(freqItemSet, minConf)
            continue
        elif (choice == 4):
            minConf = inputMinConf()
            freqItemSet = secondIteration(data, minConf)
            displayItemSet(freqItemSet, minConf)
            continue
        elif (choice == 5):
            minConf = inputMinConf()
            freqItemSet = thirdIteration(data, minConf)
            displayItemSet(freqItemSet, minConf)
            continue
        elif (choice == 6):
            continue
        elif (choice == 7):
            break
        else:
            print("\nError : the choice does not exist, please try again...")
            continue
    print("\nEnd of program")


main()
