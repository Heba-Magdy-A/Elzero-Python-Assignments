"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 001 to 010
  Topic: Introduction & Variables
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Multiple Line Comment describing the file
# --------------------------------------------------
"""
This python file contains the solutions for 
assignments from lesson 001 to 010.
It covers basic syntax, variables, data types, 
string concatenation, and type checking.
"""

# --------------------------------------------------
# Assignment 02
# Create three variables for Name, Age, and Country (all as Strings)
# --------------------------------------------------
name ="heba"
age = "20"
country = "Egypt"
# --------------------------------------------------
# Assignment 03
# Print the variables on 3 separate lines with headers
# Output required:
# Name: Heba
# Age: 20
# Country: Egypt
# --------------------------------------------------
print("name: " + name+ "\nage: " + age + "\ncountry: " + country)

# --------------------------------------------------
# Assignment 04
# Concatenate variables to produce the full message
# Output required:
# Hello, My Name Is Heba And Iam 20 Years Old and I Live in Egypt.
# --------------------------------------------------
print("Hello, My Name Is " + name + " And Iam " + age + " Years Old and I Live in " + country + ".")

# --------------------------------------------------
# Assignment 05
# Print the data type of each variable on separate lines
# --------------------------------------------------
print(type(name))
print(type(age))
print(type(country))