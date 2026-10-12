"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 033 to 037
  Topic: Operators & Type Conversion
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Print 4 different data types that evaluate to True,
# followed by 4 different data types that evaluate to False using bool()
# --------------------------------------------------

# True Evaluations
print(bool(10))
print(bool("Elzero"))
print(bool([1, 2, 3]))
print(bool(10.5))

# False Evaluations
print(bool(0))
print(bool(""))
print(bool([]))
print(bool(None))


# --------------------------------------------------
# Assignment 02
# Check if all skill percentages are greater than 50% using boolean operators (No If Condition)
# --------------------------------------------------
html = 80
css = 60
javascript = 70

print(html > 50 and css > 50 and javascript > 50)


# --------------------------------------------------
# Assignment 03
# Check number conditions using logical operators
# --------------------------------------------------
num_one = 10
num_two = 20
num = 20

# Check if num is greater than ONLY one of the other two variables, not both
print(num > num_one or num > num_two) 

# Check if num is greater than BOTH other variables
print(num > num_one and num > num_two)


# --------------------------------------------------
# Assignment 04
# Math operations, formatting float types, and type conversion
# --------------------------------------------------
num_one = 10
num_two = 20

# Store the sum of the two variables in a new variable 'result' and print it
result = num_one + num_two
print(result)

# Raise the resulting number to the power of 3
exponent_result = result ** 3
print(exponent_result)

# Find the remainder of dividing the previous number by 26000
mod_result = exponent_result % 26000
print(mod_result)

# Divide the resulting number by 5 and ensure it is a float
div_result = mod_result / 5
print(div_result)

# Convert the final result to a string and print its type
print(type(str(div_result)))