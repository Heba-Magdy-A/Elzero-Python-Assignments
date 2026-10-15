"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 056 to 059
  Topic: Functions
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Function to perform basic arithmetic operations (add, subtract, multiply)
# with flexible naming, short codes, and default operation (add).
# --------------------------------------------------
def calculate(num1, num2, operation="add"):
    # Convert operation to lowercase and strip whitespace for flexible matching
    op = str(operation).strip().lower()
    
    if op == "add" or op == "a" or op == "+":
        return num1 + num2
    elif op == "subtract" or op == "s" or op == "-":
        return num1 - num2
    elif op == "multiply" or op == "m" or op == "*":
        return num1 * num2
    else:
        return "This Operation Is Not Available"

# Tests
print(calculate(10, 20))            # 30
print(calculate(10, 20, "AdD"))     # 30
print(calculate(10, 20, "a"))       # 30
print(calculate(10, 20, "A"))       # 30
print(calculate(10, 20, "S"))       # -10
print(calculate(10, 20, "subTRACT"))# -10
print(calculate(10, 20, "Multiply"))# 200
print(calculate(10, 20, "m"))       # 200


# --------------------------------------------------
# Assignment 02
# Function accepting arbitrary arguments with special rules for 10 and 5
# --------------------------------------------------
def addition(*nums):
    result = 0
    for num in nums:
        if num == 10:
            continue
        elif num == 5:
            result -= 5
        else:
            result += num
    return result

# Tests
print(addition(10, 20, 30, 10, 15))             # 65
print(addition(10, 20, 30, 10, 15, 5, 100))     # 160


# --------------------------------------------------
# Assignment 03
# Function to display personal info and variable number of skills
# --------------------------------------------------
def show_skills(name, *skills):
    if len(skills) > 0:
        print(f"Hello {name} Your Skills Is")
        for skill in skills:
            print(f"- {skill}")
    else:
        print(f"Hello {name} You Have No Skills To Show")

# Tests
show_skills("Osama", "HTML", "CSS", "JS", "Python")
show_skills("Ahmed")


# --------------------------------------------------
# Assignment 04
# Function to say hello with default parameters for missing values
# --------------------------------------------------
def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} Your Age Is {age} And You Live In {country}"

# Tests
print(say_hello("Osama", 38, "Egypt"))
print(say_hello())