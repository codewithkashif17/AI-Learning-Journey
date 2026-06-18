# What is If Elif Else?
# if elif else is used to check multiple conditions.
# If the first condition is False,
# Python checks the next condition using elif.
# If no condition is True, the else block runs.


# Example 1: Grade Checker

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

# Explanation:
# Python checks each condition one by one.
# The first True condition runs.


# Example 2: Traffic Light System

light = "yellow"

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Ready")
elif light == "green":
    print("Go")
else:
    print("Invalid Signal")

# Explanation:
# Different messages are shown
# based on the traffic light color.


# Example 3: Number Checker

number = 0

if number > 0:
    print("Positive Number")
elif number < 0:
    print("Negative Number")
else:
    print("Zero")

# Explanation:
# The program checks whether
# the number is positive, negative, or zero.


# Example 4: Day Checker

day = 6

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
else:
    print("Weekend")

# Explanation:
# Different outputs are printed
# depending on the value of day.


# Example 5: Login System

username = "admin"

if username == "admin":
    print("Welcome Admin")
elif username == "guest":
    print("Welcome Guest")
else:
    print("Unknown User")

# Explanation:
# The program checks different usernames
# and prints the matching message.


