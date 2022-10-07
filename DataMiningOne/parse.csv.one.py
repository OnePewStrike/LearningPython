import csv

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # next(csv_reader) // moves to next line
    with open('new_data_format.csv', 'w') as new_file:
        fieldnames = ['X1', 'X2', 'X3', 'X4', 'Y']
        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter=',')

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
            # print(line[2])
            # print(line[2]) // 3rd column will be printed
