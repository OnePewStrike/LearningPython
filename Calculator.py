def sum(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    return x // y


def showMenuOptions():
    print("\n\tMain Menu")
    print("\t1. Addition")
    print("\t2. Subtraction")
    print("\t3. Multiplication")
    print("\t4. Division")
    print("\t5. Exit")
    return input("\tUser choice: ")


def showOutput(output):
    print("\n\tThe output is {}", output)


choice = 'Y'

while choice == 'y' or choice == 'Y':
    input = showMenuOptions()
    firstNum = int(input("Enter first num: "))
    secondNum = int(input("Enter second num: "))

    if (input == 1):
        output = sum(firstNum, secondNum)
        showOutput(output)
    elif (input == 2):
        output = subtract(firstNum, secondNum)
        showOutput(output)
    elif (input == 3):
        output = multiply(firstNum, secondNum)
        showOutput(output)
    elif (input == 2):
        output = division(firstNum, secondNum)
        showOutput(output)

    choice = input("\tDo you want to continue? (y/n): ")
