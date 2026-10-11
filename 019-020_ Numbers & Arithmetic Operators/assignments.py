"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 019 to 020
  Topic: Numbers & Arithmetic Operators
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Print all number types in Python (Integer, Float, Complex)
# --------------------------------------------------
print(10)          # Integer
print(10.5)        # Float
print(1 + 2j)      # Complex Number


# --------------------------------------------------
# Assignment 02
# Print Imaginary part first, then Real part of complex number (1+2j)
# Output required:
# 2.0
# 1.0
# --------------------------------------------------
complex_num = 1 + 2j

print(complex_num.imag)
print(complex_num.real)


# --------------------------------------------------
# Assignment 03
# Convert number 10 to a Float with 10 decimal places
# Needed Output:
# 10.0000000000
# --------------------------------------------------
num = 10

print(f"{float(num):.10f}")


# --------------------------------------------------
# Assignment 04
# Convert 159.650 to Integer, print value then print type
# Needed Output:
# 159
# <class 'int'>
# --------------------------------------------------
num = 159.650
int_num = int(num)

print(int_num)
print(type(int_num))


# --------------------------------------------------
# Assignment 05
# Replace '?' with correct arithmetic operators
# --------------------------------------------------
print(100 - 115)  # -15
print(50 * 30)    # 1500
print(21 % 4)     # 1
print(110 // 11)  # 10
print(97 // 20)   # 4
