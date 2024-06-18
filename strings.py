# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Getting the character at position 1 (remember that the first character has the position 0):

e = "Suellen"

print(e[1])

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in our previous a variable:

for x in e:
    print(x)

# To get the length of a string, use the len() function.

print(len(e))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"

print("free" in txt)  # This line will return the "true" bool, because the word is included in the referred phrase.
print("gate" in txt)  # This line will return the "false" bool, because the word is not included in the referred phrase.

print("free" not in txt)  # This line will return the "false" bool, because the word is included in the referred phrase.
print("gate" not in txt)  # This line will return the "true" bool, because the word is not included.

# We can also use that keyword "in" in an "if" method, like.

if "free" in txt:
    print("Yes, 'free' is on the sentence.")

if "gate" not in txt:
    print("No, 'gate' is not on the sentence.")

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

b = "Hello, World!"

# Get the characters from position 2 to position 5 (not included).
print(b[2:5])  # This line will return "llo".

# By leaving out the start index, the range will start at the first character.
print(b[:5])  # This line will return "Hello".

