"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 051 to 055
  Topic: Loop For & Training
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Extract numbers divisible by 5, print them with an automatic index 
# (descending order), and print a success message at the end.
# --------------------------------------------------
my_nums = [15, 81, 5, 17, 20, 21, 13]

# Sort numbers descending
sorted_nums = sorted(my_nums, reverse=True)
counter = 1

for num in sorted_nums:
    if num % 5 == 0:
        print(f'"{counter} => {num}"')
        counter += 1

print("All Numbers Printed")


# --------------------------------------------------
# Assignment 02
# Print numbers from 1 to 20 with zero-padding for numbers < 10,
# excluding numbers 6, 8, and 12.
# --------------------------------------------------
for num in range(1, 21):
    if num in (6, 8, 12):
        continue

    print(f'"{str(num).zfill(2)}"')

print("All Numbers Printed")


# --------------------------------------------------
# Assignment 03
# Iterate through ranks dictionary, calculate points for each subject,
# and print total points without modifying the original dictionary.
# --------------------------------------------------
my_ranks = {'Math': 'A', "Science": 'B', 'Drawing': 'A', 'Sports': 'C'}

rank_points = {
    'A': 100,
    'B': 80,
    'C': 40
}

total_points = 0

for subject, rank in my_ranks.items():
    points = rank_points[rank]
    total_points += points
    print(f'"My Rank in {subject} Is {rank} And This Equal {points} Points"')

print(f'"Total Points Is {total_points}"')


# --------------------------------------------------
# Assignment 04
# Nested dictionary iteration using items() to calculate student points
# --------------------------------------------------
students = {
    "Ahmed": {"Math": "A", "Science": "D", "Draw": "B", "Sports": "C", "Thinking": "A"},
    "Sayed": {"Math": "B", "Science": "B", "Draw": "B", "Sports": "D", "Thinking": "A"},
    "Mahmoud": {"Math": "D", "Science": "A", "Draw": "A", "Sports": "B", "Thinking": "B"}
}

rank_points = {
    'A': 100,
    'B': 80,
    'C': 40,
    'D': 20
}

for student, subjects in students.items():
    print("------------------------------")
    print(f"-- Student Name => {student}")
    print("------------------------------")
    
    total_student_points = 0
    for subject, rank in subjects.items():
        points = rank_points[rank]
        total_student_points += points
        print(f"- {subject} => {points} Points")
        
    print(f"Total Points For {student} Is {total_student_points}")

print("------------------------------")