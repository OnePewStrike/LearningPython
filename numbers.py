a = 5

print(type(a))

print(type(5.0))

c = 5 + 3j
print(c + 3)

print(isinstance(c, complex))

# Output: 107
print(0b1101011)

# Output: 253 (251 + 2)
print(0xFB + 0b10)

# Output: 13
print(0o15)

import decimal

print(0.1)

print(decimal.Decimal(0.1))

from decimal import Decimal as D

print(D('1.1') + D('2.2'))

print(D('1.2') * D('2.50'))

import fractions

print(fractions.Fraction(1.5))

print(fractions.Fraction(5))

print(fractions.Fraction(1,3))

import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))

import random

print(random.randrange(10, 20))

x = ['a', 'b', 'c', 'd', 'e']

# Get random choice
print(random.choice(x))

# Shuffle x
random.shuffle(x)

# Print the shuffled x
print(x)

# Print random element
print(random.random())