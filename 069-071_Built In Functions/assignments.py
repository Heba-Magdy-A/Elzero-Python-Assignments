"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 069 to 071
  Topic: Built-In Functions
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Analyze code behavior, conditions, and explain outputs
# --------------------------------------------------

# Tuple containing numbers
values = (0, 1, 2)

# any() returns True because at least one element (1 or 2) is truthy (not 0)
if any(values):
    # This block executes, so my_var is created and assigned 0
    my_var = 0

# A list containing various data types including my_var (which is 0)
my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

# Checking conditions using all() function:
# 1. all(my_list[:4]) -> Checks first 4 elements [True, 1, 1, ["A", "B"]]. All are truthy -> True.
# Since the first condition is True, the 'or' chain short-circuits and evaluates to True.
if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):
    print("Good")  # Output => Good
else:
    print("Bad")


# --------------------------------------------------
# Assignment 02
# Find the value of v that makes the output 820
# --------------------------------------------------
v = 40

my_range = list(range(v)) 
print(sum(my_range, v) + pow(v, v, v))  # Output => 820


# --------------------------------------------------
# Assignment 03
# Find the value of variable n
# --------------------------------------------------
n = 21

l = list(range(n)) 
if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
    print("Good")  # Output => Good


# --------------------------------------------------
# Assignment 04
# Custom implementations of all(), any(), min(), and max() functions
# supporting both lists and tuples.
# --------------------------------------------------

def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

def my_any(iterable):
    for element in iterable:
        if element:
            return True
    return False

def my_min(iterable):
    minimum = iterable[0]
    for element in iterable:
        if element < minimum:
            minimum = element
    return minimum

def my_max(iterable):
    maximum = iterable[0]
    for element in iterable:
        if element > maximum:
            maximum = element
    return maximum

# Tests for Assignment 04
print(my_all([1, 2, 3]))                    # True
print(my_all([1, 2, 3, []]))                # False
print(my_any([0, 1, [], False]))            # True
print(my_any([(), 0, False]))               # False
print(my_min([10, 100, -20, -100, 50]))     # -100
print(my_min((10, 100, -20, -100, 50)))     # -100
print(my_max([10, 100, -20, -100, 50, 700]))# 700
print(my_max((10, 100, -20, -100, 50, 700)))# 700