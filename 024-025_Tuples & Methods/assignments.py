"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 024 to 025
  Topic: Tuples & Methods
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Create a tuple with a single element without parentheses, then print it and its type
# --------------------------------------------------
my_tuple = "Heba",

print(my_tuple[0])
print(type(my_tuple))


# --------------------------------------------------
# Assignment 02
# Change the first element of a tuple by converting it to a list and back, 
# then print the tuple, its type, and its length
# --------------------------------------------------
friends = ("Osama", "Ahmed", "Sayed")

friends_list = list(friends)
friends_list[0] = "Elzero"
friends = tuple(friends_list)

print(friends)
print(type(friends))
print(f"{len(friends)} Elements")


# --------------------------------------------------
# Assignment 03
# Concatenate two tuples (numbers and letters) and print the result and length
# --------------------------------------------------
nums = (1, 2, 3)
letters = ("A", "B", "C")

nums_and_letters_one = nums + letters
print(nums_and_letters_one)
print(f"{len(nums_and_letters_one)} Elements")


# --------------------------------------------------
# Assignment 04
# Destructure a tuple of 4 elements in a single line (ignoring the 3rd element)
# --------------------------------------------------
my_tuple = (1, 2, 3, 4)

a, b, _, c = my_tuple

print(a)
print(b)
print(c)