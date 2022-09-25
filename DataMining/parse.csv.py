import csv

# with open('new_data_format.csv', 'r') as csv_file:
#   csv_reader = csv.reader(csv_file, delimiter="\t")
  
#   for line in csv_reader:
#     print(line)
  
with open('data.csv', 'r') as csv_file:
  csv_reader = csv.DictReader(csv_file)
  
  for line in csv_reader:
    # print(line)
    print(line['X1'])
  
  
# with open('data.csv', 'r') as csv_file:
#   csv_reader = csv.reader(csv_file)
  
#   # next(csv_reader) // moves to next line
#   with open('new_data_format.csv', 'w') as new_file:
#     csv_writer = csv.writer(new_file, delimiter='\t')
  
#     for line in csv_reader:
#       csv_writer.writerow(line)
#       #print(line[2])
#       # print(line[2]) // 3rd column will be printed