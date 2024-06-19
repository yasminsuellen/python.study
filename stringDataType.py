# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Getting the character at position 1 (remember that the first character has the position 0):

a = "The best things in life are free!"

print(a[1])
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in our previous a variable:

for x in a:
    print(x)

# To get the length of a string, use the len() function.

print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

print("free" in a)  # This line will return the "true" bool, because the word is included in the referred phrase.
print("gate" in a)  # This line will return the "false" bool, because the word is not included in the referred phrase.

print("free" not in a)  # This line will return the "false" bool, because the word is included in the referred phrase.
print("gate" not in a)  # This line will return the "true" bool, because the word is not included.

# We can also use that keyword "in" in an "if" method, like.

if "free" in a:
    print("Yes, 'free' is on the sentence.")

if "gate" not in a:
    print("No, 'gate' is not on the sentence.")

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Get the characters from position 2 to position 5 (not included).
print(a[2:5])

# By leaving out the start index, the range will start at the first character.
print(a[:5])

# By leaving out the end index, the range will go to the end.
print(a[2:])

# The upper() method returns the string all in upper case.
print(a.upper())

# The lower() method returns the string in lower case.
print(a.lower())

# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

b = "   The best things in life are free!   "
print(b.strip())

# The replace() method replaces a string with another string.
print(a.replace("e", "*"))

# The split() method returns a list where the text between the specified separator becomes the list items.
print(a.split(" "))

# To concatenate, or combine, two strings you can use the + operator.
print(a + b)

# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings. To specify a string as
# an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for
# variables and other operations.

age = 36
txt = "My name is John, I am"
conbinedTxt = f"My name is John, I am {age}"

print(conbinedTxt)
print(txt, age)  # That is another way to do almost the same thing.

# A placeholder can include a modifier to format the value. A modifier is included by adding a colon : followed by a
# legal formatting type, like .2f which means fixed point number with 2 decimals:

price = 59
txt1 = f"The price is {price:.2f} dollars"
print(txt1)

# A placeholder can contain Python code, like math operations:

txt2 = f"The price is {10 * 5} dollars"
print(txt2)

""" 
String methods ->

capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
"""