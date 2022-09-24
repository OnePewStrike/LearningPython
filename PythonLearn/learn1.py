drink = "Available"
food = None


def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)


menu(drink)
menu(food)

fruits = ["apple", "mango", "orange"]  # list
numbers = (1, 2, 3)  # tuple
alphabets = {'a': 'apple', 'b': 'ball', 'c': 'cat'}  # dictionary
vowels = {'a', 'e', 'i', 'o', 'u'}  # set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))

a = [5, 10, 15, 20, 25, 30, 35, 40]

print(a)
# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

a = [1, 2, 3]
a[2] = 4
print(a)

t = (5, 'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10
