"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 011 to 018
  Topic: Strings & Methods
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Concatenate variables with escape characters to produce the exact output
# Output required:
# "Hello 'Osama', How You Doing \
# "" Your Age Is "38" "" +
# And Your Country Is : Egypt
# --------------------------------------------------
name = "Heba"
age = "20"
country = "Egypt"

print(f'"Hello \'{name}\', How You Doing \\\n"" Your Age Is "{age}" "" +\nAnd Your Country Is : {country}')


# --------------------------------------------------
# Assignment 02
# Print the same message on multiple lines using triple quotes or escape chars
# Output required:
# "Hello 'Osama', How You Doing \
# "" Your Age Is "38" "" +
# And Your Country Is : Egypt
# --------------------------------------------------
print(f""""Hello '{name}', How You Doing \\
"" Your Age Is "{age}" "" +
And Your Country Is : {country}""")


# --------------------------------------------------
# Assignment 03
# Indexing + Slicing dynamically
# Needed Output:
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"
# --------------------------------------------------
name = 'Elzero'

print(f'Second Letter Is "{name[1]}"')
print(f'Third Letter Is "{name[2]}"')
print(f'Last Letter Is "{name[-1]}"')


# --------------------------------------------------
# Assignment 04
# Extract specific slices dynamically
# Needed Output:
# "lze"
# "Ezr"
# "rzE"
# --------------------------------------------------
name = 'Elzero'

print(f'"{name[1:4]}"')
print(f'"{name[0::2]}"')
print(f'"{name[-2::-2]}"')


# --------------------------------------------------
# Assignment 05
# Strip unwanted characters
# Needed Output:
# Elzero
# --------------------------------------------------
name = "#@#@Elzero#@#@"

print(name.strip("#@"))


# --------------------------------------------------
# Assignment 06
# Zero padding up to 4 digits
# Needed Output:
# 0009
# 0015
# 0130
# 0950
# 1500
# --------------------------------------------------
num1 = "9"
num2 = "15"
num3 = "130"
num4 = "950"
num5 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
print(num5.zfill(4))


# --------------------------------------------------
# Assignment 07
# Right-align with `@` padding up to 20 chars
# Needed Output:
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero
# --------------------------------------------------
name_one = "Heba"
name_two = "Heba_Magdy"

print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))


# --------------------------------------------------
# Assignment 08
# Swap cases (upper to lower, lower to upper)
# Needed Output:
# osAMa
# OSAma
# --------------------------------------------------
name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())


# --------------------------------------------------
# Assignment 09
# Count occurrence of a substring
# Needed Output:
# 2
# --------------------------------------------------
msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))


# --------------------------------------------------
# Assignment 10
# Find position of character 'z'
# Needed Output:
# 2
# --------------------------------------------------
name = "Elzero"

print(name.index("z"))


# --------------------------------------------------
# Assignment 11
# Replace '<3' with 'Love' once
# Needed Output:
# I Love Python And Although <3 Elzero Web School
# --------------------------------------------------
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love", 1))


# --------------------------------------------------
# Assignment 12
# Replace all occurrences of '<3' with 'Love'
# Needed Output:
# I Love Python And Although Love Elzero Web School
# --------------------------------------------------
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love"))


# --------------------------------------------------
# Assignment 13
# Format output using f-strings with integer age
# Needed Output:
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt
# --------------------------------------------------
name = "Heba"
age = 20
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")