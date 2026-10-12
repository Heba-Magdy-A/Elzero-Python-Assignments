"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 038 to 040
  Topic: User Input & Practice
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Get name from user, strip whitespace, capitalize first letter, and print welcome message
# --------------------------------------------------
name = input("Enter Your Name: ").strip().capitalize()

print(f"Hello {name}, Happy To See You Here.")


# --------------------------------------------------
# Assignment 02
# Get age from user as integer, check if under 16 or 16+ and print appropriate message
# --------------------------------------------------
age = int(input("Enter Your Age: "))

if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


# --------------------------------------------------
# Assignment 03
# Get first and second names, clean them, and print first name with first letter of second name
# --------------------------------------------------
first_name = input("Enter Your First Name: ").strip().capitalize()
second_name = input("Enter Your Second Name: ").strip().capitalize()

print(f"Hello {first_name} {second_name:.1s}.")


# --------------------------------------------------
# Assignment 04
# Get email, parse username, service provider, and top-level domain
# --------------------------------------------------
email = input("Enter Your Email: ").strip().lower()

name_part = email[:email.index("@")]
service_provider = email[email.index("@") + 1 : email.rindex(".")]
tld = email[email.rindex(".") + 1 :]

print(f"Your Name Is {name_part.capitalize()}")
print(f"Email Service Provider Is {service_provider}")
print(f"Top Level Domain Is {tld}")