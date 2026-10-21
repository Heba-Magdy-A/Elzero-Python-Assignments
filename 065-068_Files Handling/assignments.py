"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 065 to 068
  Topic: Files Handling (Simple & Without With-As)
==================================================
"""

import os

# Set up paths cleanly
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
folder = os.path.join(desktop, "Python")

# Ensure directory exists and navigate to it
if not os.path.exists(folder):
    os.makedirs(folder)
os.chdir(folder)

# --------------------------------------------------
# Assignment 01: Create 50 files and handle special file
# --------------------------------------------------
for i in range(1, 51):
    if i == 25:
        file_name = "special-text.txt"
        file = open(file_name, "w")
        file.close()
    else:
        file_name = f"txt{i}.txt"
        file = open(file_name, "w")
        file.write(f"Elzero Web School => {i}")
        file.close()

print(os.getcwd())
print(os.path.abspath(__file__))
print(os.path.basename(__file__))
print(len(os.listdir(folder)))


# --------------------------------------------------
# Assignment 02: Append lines to txt1.txt
# --------------------------------------------------
file_one = open("txt1.txt", "a")
for _ in range(50):
    file_one.write("\nAppended => Elzero Web School")
file_one.close()


# --------------------------------------------------
# Assignment 03: Read and analyze txt1.txt content
# --------------------------------------------------
file_one = open("txt1.txt", "r")
content = file_one.read()
file_one.close()

# Read lines separately for line count
file_one = open("txt1.txt", "r")
lines = file_one.readlines()
file_one.close()

print(f"Number Of Lines Is => {len(lines)}")
print(f"Number Of Words Is => {len(content.split())}")
print(f"Number Of Chars Is => {len(content)}")
print(f'Number Of "l" Char Is => {content.lower().count("l")}')


# --------------------------------------------------
# Assignment 04: Delete the last 10 text files
# --------------------------------------------------
for i in range(41, 51):
    file_to_remove = f"txt{i}.txt"
    if os.path.exists(file_to_remove):
        os.remove(file_to_remove)