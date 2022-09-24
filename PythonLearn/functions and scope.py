def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")


greet('Paul')


def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))

print(absolute_value(-4))


def my_func():
	x = 10
	print("Value inside function:", x)


x = 20
my_func()
print("Value outside function:", x)
