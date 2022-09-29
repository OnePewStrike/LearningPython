import csv

# with open('new_data_format.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter="\t")

#     for line in csv_reader:
#         print(line)

# with open('data.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         # print(line)
#         print(line['X1'])


with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # next(csv_reader) // moves to next line
    with open('new_data_format.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter=',')

        for line in csv_reader:
            csv_writer.writerow(line)
            print(line[2])
            # print(line[2]) // 3rd column will be printed

            #  with open('new_data_format.csv', 'w') as new_file:
            #      csv_writer = csv.write(new_file)

            #      for line in csv_reader:
            #          if (line[i] == ''):
            #              del line[i]


# next(csv_reader)
# for row in csv_reader:
#     for index in range(0, 4):
#         if row[index] == '':
#             solveIndex(index, prev_row, position, L)
#             print("CHECK PREVIOUS ROW:", prev_row)
#     L.append(row)
#     prev_row = row
#     position += 1

#  next(csv_reader)
#   for row in csv_reader:
#        if (isNext == True):
#             after = float(row[1])
#             mean = (after + prev) / 2
#             prev_row[1] = str(mean)
#             print("CHECK: ", after, prev, mean)
#             input("Enter to continue..")
#             L.append(prev_row)
#             L.append(row)
#             print("CHECK PREVIOUS ROW: ", prev_row)
#             print("CHECK AFTER ROW: ", row)
#             print(row)
#             isNext = False
#             isFound = False
#             break
#         else:
#             for index in range(0, 4):
#                 if row[index] == '':
#                     isFound = True
#                     break
#             if (isFound == True):
#                 isNext = True
#                 isFound = False
#                 continue
#             else:
#                 isNext = False
#                 isFound = False
#             L.append(row)
#             prev_row = row
#             prev = float(prev_row[1])

# next(csv_reader)
# for row in csv_reader:
#     if row[0] == '':
#         L = solveIndex(0, prev_row, position, L)
#         print("CHECK PREVIOUS ROW:", prev_row)
#         prev_row = row
#         position += 1
#         continue
#     L.append(row)
#     prev_row = row
#     position += 1

            # print("CHECK PREVIOUS: ", prev_row)
            # print("CHECK TARGET ROW: ", target_row)
            # print("CHECK CURRENT: ", row)
            # input("Enter to continue..")
            # print("CHECK VALUES: ", after, prev, mean)
