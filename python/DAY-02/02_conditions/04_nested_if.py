
# What is Nested If?
# Nested if means an if statement inside another if statement.
# It is used when one condition depends on another condition.


# Example 1: Age and License Check

age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a driving license")
else:
    print("You are too young to drive")

# Explanation:
# First age is checked.
# If age condition is True, then license is checked inside it.


# Example 2: Login System

username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

# Explanation:
# First username is checked.
# If correct, then password is checked.


# Example 3: Number Check

number = 10

if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Number is zero or negative")

# Explanation:
# First number is checked positive or not.
# Then it is checked even or odd inside it.


# Example 4: Exam Result

marks = 75

if marks >= 50:
    if marks >= 80:
        print("Pass with A Grade")
    else:
        print("Pass")
else:
    print("Fail")

# Explanation:
# First pass/fail is checked.
# Then grade is checked inside pass condition.


# Example 5: Weather Check

temperature = 35

if temperature > 30:
    if temperature > 40:
        print("Very Hot Weather")
    else:
        print("Hot Weather")
else:
    print("Normal Weather")

# Explanation:
# First temperature is checked.
# Then detailed condition is checked inside it.

