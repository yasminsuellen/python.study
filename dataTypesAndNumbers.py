# In programming, data type is an important concept.
# Variables can store data of different types, and different types can do different things.
# Python has the following data types built-in by default, in these categories:

"""
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
None Type: NoneType
"""

x = "Hello World"  # Setting a data type.
y = str("Hello World")  # Setting a specific data type.

# Python Numbers
# There are three numeric types in Python: int, float and complex.

x = 1  # Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
y = 2.8  # Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

# Float can also be scientific numbers with an "e" to indicate the power of 10.

z = 1j  # Complex numbers are written with a "j" as the imaginary part.

# You can convert from one type to another with the name of the tipe in methods like: int(), float(), and complex().

a = float(x)  # convert from int to float.
b = int(y)  # convert from float to int.
c = complex(x)  # convert from int to complex.
d = str(x)  # convert from int to string.

# Python does not have a random() function to make a random number, but Python has a built-in module called
# random that can be used to make random numbers.

import random

print(random.randrange(1, 10))