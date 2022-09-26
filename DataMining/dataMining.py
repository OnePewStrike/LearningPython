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
     
    with open('data.csv', 'r') as csv_file: 
        csv_reader = csv.reader(csv_file) 
  
        X1 = str(getAverage(0))
        X2 = str(getAverage(1))
        X3 = str(getAverage(2))
        X4 = str(getAverage(3))
        Y = str(getAverage(4))
         
        for row in csv_reader: 
            if row[0] == '': 
                row[0] = X1
            if row[1] == '': 
                row[1] = X2
            if row[2] == '': 
                row[2] = X3
            if row[3] == '': 
                 row[3] = X4
            if row[4] == '': 
                  row[4] = Y
            else: 
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
            if row[0] == '' or row[1] == '' or row[2] == '' or row[3] == '' or row[4] == '': 
                continue 
            average += float(row[index])
            count += 1
        total = average / count 
    return str(total)
    
def solveByGlobalConstant(): 
    L = [] 
    with open('data.csv', 'r') as csv_file: 
        csv_reader = csv.reader(csv_file) 
  
        for row in csv_reader: 
            if row[0] == '': 
                row[0] = '0'
            if row[1] == '': 
                row[1] = '0'
            if row[2] == '': 
                row[2] = '0'
            if row[3] == '': 
                row[3] = '0'
            if row[4] == '': 
                row[4] = '0'
            else: 
                L.append(row) 
  
        for row in csv_reader:
            print(row[0])

        with open("new_data_format.csv", 'w') as new_file: 
             csv_writer = csv.writer(new_file, delimiter=",") 
             csv_writer.writerows(L)
 
def solveByLinearInter():  
    L = [] 
    prev = 0
    next = 0
    mean = 0.0
    
    with open('data.csv', 'r') as csv_file: 
        csv_reader = csv.reader(csv_file) 
  
        for row in csv_reader: 
            if row[0] == '':
                next(csv_reader)
                next = float(row[0])
                mean = (next + prev) / 2
                L.append(mean)
                break
            else:
                L.append(row[0])
            prev = float(row[0])
        
            with open("new_data_format.csv", 'w') as new_file: 
             csv_writer = csv.writer(new_file, delimiter=",") 
             csv_writer.writerows(L)

def showMenuOptions():
    print("\n\tMain Menu")
    print("\t1. Show original data")
    print("\t2. Solve by removing rows with missing data")
    print("\t3. Solve by average")
    print("\t4. Solve by linear interpolation")
    print("\t5. Solve by global constant")
    print("\t6. Exit")
    x = int(input("\tUser choice: "))
    return x


solveByAverage()

# while True:   
#     choice = int(showMenuOptions())
#     if (choice == 1):
#         # viewOriginalData()
#         continue
#     elif (choice == 2):
#         # solveByRemoveRows()
#         continue
#     elif (choice == 3):
#         # solveByAverage()
#         continue
#     elif (choice == 4):
#         # solveByLinearInter()
#         continue
#     elif (choice == 5):
#         # solveByGlobalConstant()
#         continue
#     elif (choice == 6):
#         break
#     else:
#         print("\tError: choice does not exist...")
#         continue
# print("\tEnd of progtam")