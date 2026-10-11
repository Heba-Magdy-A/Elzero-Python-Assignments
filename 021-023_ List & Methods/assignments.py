"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 021 to 023
  Topic: List & Methods
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Print first friend and last friend using two different methods for each
# --------------------------------------------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

# Method One & Two for First Friend ("Osama")
print(f'"{friends[0]}" => Method One')
print(f'"{friends.copy().pop(0)}" => Method Two') # Or friends[::5][0] / next valid method

# Method One & Two for Last Friend ("Mahmoud")
print(f'"{friends[-1]}" => Method One')
print(f'"{friends.pop()}" => Method Two')


# --------------------------------------------------
# Assignment 02
# Print odd index names in first line, even index names in second line
# --------------------------------------------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[0::2])
print(friends[1::2])


# --------------------------------------------------
# Assignment 03
# Print elements from index 2 to 4, and the last two elements dynamically
# --------------------------------------------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

print(friends[1:4])
print(friends[-2:])


# --------------------------------------------------
# Assignment 04
# Update the last two names in the list to "Elzero"
# --------------------------------------------------
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]

friends[-2:] = ["Elzero", "Elzero"]
print(friends)


# --------------------------------------------------
# Assignment 05
# Add a name to the beginning and another name to the end
# --------------------------------------------------
friends = ["Osama", "Ahmed", "Sayed"]

friends.insert(0, "Nasser")
print(friends)

friends.append("Salem")
print(friends)


# --------------------------------------------------
# Assignment 06
# Remove first two names, then remove the last name
# --------------------------------------------------
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]

friends.remove("Nasser")
friends.remove("Osama")
print(friends)

friends.pop()
print(friends)


# --------------------------------------------------
# Assignment 07
# Concatenate multiple lists together
# --------------------------------------------------
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]

all_friends = friends + employees + school
print(all_friends)


# --------------------------------------------------
# Assignment 08
# Sort the list alphabetically (A to Z) and reverse-alphabetically (Z to A)
# --------------------------------------------------
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

friends.sort()
print(friends)

friends.sort(reverse=True)
print(friends)


# --------------------------------------------------
# Assignment 09
# Count the number of items inside the list
# --------------------------------------------------
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]

print(len(friends))


# --------------------------------------------------
# Assignment 10
# Nested lists and accessing elements inside sub-lists dynamically
# --------------------------------------------------
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]

print(technologies[-1][0])
print(technologies[-1][-1])