"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 047 to 050
  Topic: While Loop & Training
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Print numbers downwards from input (excluding itself and 0, skipping 6),
# and count total printed numbers.
# --------------------------------------------------
num = int(input("Enter A Number: "))

if num <= 0:
    print(f"Number {num} Is Not Larger Than 0")
else:
    printed_count = 0
    while num > 1:
        num -= 1
        if num == 6:
            continue
        print(num)
        printed_count += 1
    print(f"{printed_count} Numbers Printed Successfully.")


# --------------------------------------------------
# Assignment 02
# Print names from list using while loop, ignoring names starting with lowercase,
# and count the ignored names programmatically.
# --------------------------------------------------
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
index = 0
ignored_count = 0

while index < len(friends):
    if friends[index][0].islower():
        ignored_count += 1
    else:
        print(friends[index])
    
    index += 1  
print(f"Friends Printed And Ignored Names Count Is {ignored_count}")

# --------------------------------------------------
# Assignment 03
# Print contents of the list completely using a while loop in one line
# --------------------------------------------------
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills: print(f'"{skills.pop(0)}"')


# --------------------------------------------------
# Assignment 04
# Add friends to a limited list (max 4) with validation rules using while loop
# --------------------------------------------------
my_friends = []
max_friends = 4

while len(my_friends) < max_friends:
    name = input("Enter Friend Name: ").strip()
    
    if name.isupper():
        print("Invalid Name")
    elif name.islower():
        formatted_name = name.capitalize()
        my_friends.append(formatted_name)
        print(f"Friend {formatted_name} Added => 1st Letter Become Capital")
        print(f"Names Left in List Is {max_friends - len(my_friends)}")
    else:
        my_friends.append(name)
        print(f"Friend {name} Added")
        print(f"Names Left in List Is {max_friends - len(my_friends)}")