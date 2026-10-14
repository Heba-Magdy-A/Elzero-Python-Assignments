"""
==================================================
  Elzero Web Academy - Python Course
  Assignments: Lessons 041 to 046
  Topic: Control Flow
==================================================
"""

# --------------------------------------------------
# Assignment 01
# Simple Calculator based on user input for numbers and operation
# --------------------------------------------------
num1 = int(input("Enter First Number: ").strip())
num2 = int(input("Enter Second Number: ").strip())
operation = input("Enter Operation (+, -, *, /, %): ").strip()

if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    print(f"{num1} / {num2} = {num1 / num2}")
elif operation == "%":
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Invalid Operation")


# --------------------------------------------------
# Assignment 02
# Ternary conditional operator to check age suitability
# --------------------------------------------------
age = 17

print("App Is Suitable For You") if age > 16 else print("App Is Not Suitable For You")


# --------------------------------------------------
# Assignment 03
# Calculate age in months, weeks, days, hours, minutes, and seconds
# --------------------------------------------------
age = int(input("Enter Your Age In Years: "))

if 10 < age < 100:
    months = age * 12
    weeks = months * 4  # or age * 52
    days = age * 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60

    print(f"Your Age In Months Is {months} Months")
    print(f"Your Age In Weeks Is {weeks} Weeks")
    print(f"Your Age In Days Is {days} Days")
    print(f"Your Age In Hours Is {hours} Hours")
    print(f"Your Age In Minutes Is {minutes} Minutes")
    print(f"Your Age In Seconds Is {seconds} Seconds")
else:
    print("Your Age Is Out Of Range")


# --------------------------------------------------
# Assignment 04
# Country discount eligibility checker
# --------------------------------------------------
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

country = input("Input Your Country: ").strip().capitalize()

if country in countries:
    final_price = price - discount
    print(f"Your Country Eligible For Discount And The Price After Discount Is ${final_price}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")