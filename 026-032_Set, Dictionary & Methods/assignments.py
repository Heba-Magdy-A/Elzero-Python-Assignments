"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 026 to 032
  Topic: Set, Dictionary & Methods
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Extract unique values from a list, print the list, 
# its type, and print it without the last element
# --------------------------------------------------
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = list(set(my_list))

print(unique_list)
print(type(unique_list))
print(unique_list[:-1])


# --------------------------------------------------
# Assignment 02
# Merge two sets using three different methods
# --------------------------------------------------
nums = {1, 2, 3}
letters = {"A", "B", "C"}

# Method 1: union() method
print(nums.union(letters))

# Method 2: pipe operator (|)
print(nums | letters)

# Method 3: update() method
nums_copy = nums.copy()
nums_copy.update(letters)
print(nums_copy)


# --------------------------------------------------
# Assignment 03
# Set operations: clearing, adding, and safe removal
# --------------------------------------------------
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)

# Clear my_set in a single line and print it
my_set.clear()
print(my_set)

# Add "A" and "B" to my_set then print it
my_set.update({"A", "B"})
print(my_set)

# Try removing "C" safely (it doesn't exist, so no error should occur)
my_set.discard("C")


# --------------------------------------------------
# Assignment 04
# Check if all elements of set_one exist in set_two
# --------------------------------------------------
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}

print(set_one.issubset(set_two))


# --------------------------------------------------
# Assignment 05
# Create a dictionary of programming skills, print progress without loops, 
# and add a new skill
# --------------------------------------------------
my_skills = {
    "HTML": "90%",
    "CSS": "80%",
    "Python": "30%"
}

print(f'"HTML Progress Is {my_skills["HTML"]}"')
print(f'"CSS Progress Is {my_skills["CSS"]}"')
print(f'"Python Progress Is {my_skills["Python"]}"')

# Add a new skill and print its progress
my_skills["AI"] = "20%"
print(f'"AI Progress Is {my_skills["AI"]}"')