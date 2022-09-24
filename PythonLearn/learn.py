import constant
print("Test")
print('*' * 10)

price = 10
print(price)

rating = 4.9
name = "John Smith"
age = 20

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

print(a)

for i in range(1, 11):
    print(i)
    if i == 5:
        break

if True:
    print('Hello')
    a = 5

# single-line comment
"""Multi-line comment"""


def double(num):
    """Function to double the value"""
    return 2*num


print(double.__doc__)

a, b, c = 5, 3.2, "Hello"

print(a)
print(b)
print(c)

print(constant.PI)
print(constant.GRAVITY)

a = 0b1010  # Binary Literals
b = 100  # Decimal Literal
c = 0o310  # Octal Literal
d = 0x12c  # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
