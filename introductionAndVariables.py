# This file will be used to store the notations and experiments of language study in Python.

# Comments can be placed at the end of a line, and Python will ignore the rest of the line.

print("After that there is a ridden line of comment -> [???]")  # This is a comment.

# In other languages, indentation is used for readability only. In Python, indentation is used to indicate a block of
# code. If it is not used properly, the terminal will return an error.

if 5 > 2:
    print("Conditional test ran sucessfuly -> Five is greater than two!")

# Variables are containers for storing data values. In Python there is no reserved word for declaring variables.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type, and can even change type after they have been set.

print("Setting value to variables x and y.")

x = 5
y = "Antonio"

print("Variable x ->", x)
print("Variable y ->", y)

# Variables can change type and value after they have been set.

print("Changing value and type to variables x and y.")

x = "Leonardo"
y = 6

print("Variable x ->", x)
print("Variable y ->", y)

# If you want to specify the data type of variable, this can be done with casting.
# You can get the data type of variable with the type() function.
# Variable names are case-sensitive -> the variable X is different from the variable x.

print("Resetting value to variables x, y and creating a variable z.")

x = str(3)
y = int(3)
z = float(3)

print("Variable x as a str ->", x)
print("Variable y as a int ->", y)
print("Variable z as a float ->", z)

print(type(y))
print(type(x))
print(type(z))

# A variable name must start with a letter or the underscore character. A variable name can only contain
# alphanumeric characters and underscores (A-z, 0-9, and _ ). Variable names with more than one word can be difficult
# to read. There are several techniques you can use to make them more readable, for example Camel Case.

myVariableName = "John"

# Python allows you to assign values to multiple variables in one line.

print("Resetting value to variables x, y and z.")

x, y, z = "Orange", "Banana", "Cherry"

print("Variable x ->", x)
print("Variable y ->", y)
print("Variable z ->", z)

# And you can assign the same value to multiple variables in one line:

print("Resetting value to variables x, y and z.")

x = y = z = "strawberry"

print("Variable x ->", x)
print("Variable y ->", y)
print("Variable z ->", z)

# If you have a collection of values in a list. Python allows you to extract the values into variables.
# This is called unpacking.

fruits = ["apple", "banana", "cherry"]

print("Resetting value to variables x, y and z.")

x, y, z = fruits

print("Variable x ->", x)
print("Variable y ->", y)
print("Variable z ->", z)

# The Python print() function is often used to output variables.
# In the print() function, you output multiple variables, separated by a comma.
# You can also use the + operator to output multiple variables. For numbers, the + character works as a mathematical
# operator. In the print() function, when you try to combine a string and a number with the + operator,
# Python will give you an error. The best way to output multiple variables in the print() function is to separate
# them with commas, which even support different data types.

print(x, y, z)
print(x + y + z)

# Variables that are created outside a function are known as global variables. Global variables can be used by
# everyone, both inside of functions and outside.

x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used
# inside the function. The global variable with the same name will remain as it was, global and with the
# original value.

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)


# Normally, when you create a variable inside a function, that variable is local, and can only be used
# inside that function. To create a global variable inside a function, you can use the global keyword.
# If you use the global keyword, the variable belongs to the global scope.

def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
# To change the value of a global variable inside a function, refer to the variable by using the global keyword.

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)