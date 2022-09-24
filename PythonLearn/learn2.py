s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
# s[5] = 'd'

a = {1, 2, 2, 3, 3, 3}
print(a)

d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
#print("d[2] = ", d[2])

float(5)
int(10.6)

set([1, 2, 3])
{1, 2, 3}
tuple({5, 6, 7})
(5, 6, 7)
list('hello')
dict([[1, 2], [3, 4]])
dict([(3, 26), (4, 44)])
num_int = 123
num_str = "456"

print("Data type of num_int:", type(num_int))
print("Data type of num_str before Type Casting:", type(num_str))

num_str = int(num_str)
print("Data type of num_str after Type Casting:", type(num_str))

num_sum = num_int + num_str

print("Sum of num_int and num_str:", num_sum)
print("Data type of the sum:", type(num_sum))
