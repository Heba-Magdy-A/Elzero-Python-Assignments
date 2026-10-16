"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 060 to 064
  Topic: Packing, Recursion, Lambda
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Function using **kwargs to accept any number of keyword arguments 
# and print each key and value in the required format.
# --------------------------------------------------
def get_score(**scores):
    for subject, score in scores.items():
        print(f'"{subject} => {score}"')

# Tests
print("--- Test 01 ---")
get_score(Math=90, Science=80, Language=70)

print("\n--- Test 02 ---")
get_score(Logic=70, Problems=60)


# --------------------------------------------------
# Assignment 02
# Function accepting a name (optional) and arbitrary keyword arguments (**scores).
# Handles cases with/without name and with/without scores.
# --------------------------------------------------
def get_people_scores(name="", **scores):
    if name and len(scores) > 0:
        print(f'"Hello {name} This Is Your Score Table:"')
        for subject, score in scores.items():
            print(f'"{subject} => {score}"')
    elif name and len(scores) == 0:
        print(f'"Hello {name} You Have No Scores To Show"')
    elif not name and len(scores) > 0:
        for subject, score in scores.items():
            print(f'"{subject} => {score}"')

# Tests
print("\n--- Assignment 02 Tests ---")
print("Test 1:")
get_people_scores("Osama", Math=90, Science=80, Language=70)

print("\nTest 2:")
get_people_scores("Mahmoud", Logic=70, Problems=60)

print("\nTest 3:")
get_people_scores(Logic=70, Problems=60)

print("\nTest 4:")
get_people_scores("Ahmed")


# --------------------------------------------------
# Assignment 03
# Dictionary containing score data and a function 
# to unpack and display scores based on optional name and scores.
# --------------------------------------------------
scores_list = {
    "Math": 90,
    "Science": 80,
    "Language": 70
}

def get_the_scores(name="", **scores):
    if name and len(scores) > 0:
        print(f'"Hello {name} This Is Your Score Table:"')
        for subject, score in scores.items():
            print(f'"{subject} => {score}"')
    elif name and len(scores) == 0:
        print(f'"Hello {name} You Have No Scores To Show"')
    elif not name and len(scores) > 0:
        for subject, score in scores.items():
            print(f'"{subject} => {score}"')

# Tests
print("\n--- Assignment 03 Tests ---")
print("Test 1:")
get_the_scores("Osama", **scores_list)

print("\nTest 2:")
get_the_scores("Osama")

print("\nTest 3:")
get_the_scores(**scores_list)