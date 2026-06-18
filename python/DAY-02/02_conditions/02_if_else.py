
# What is an If Else Statement?
# if else is used to make decisions in Python.
# If the condition is True, the if block runs.
# Otherwise, the else block runs.


# Example 1: Age Check

age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Explanation:
# If age is 18 or more, the first message prints.
# Otherwise, the second message prints.


# Example 2: Even or Odd Number

number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Explanation:
# If the remainder is 0, the number is even.
# Otherwise, the number is odd.


# Example 3: Pass or Fail

marks = 40

if marks >= 50:
    print("Pass")
else:
    print("Fail")

# Explanation:
# If marks are 50 or greater, the student passes.
# Otherwise, the student fails.


# Example 4: Positive or Negative Number

num = -5

if num > 0:
    print("Positive Number")
else:
    print("Negative Number")

# Explanation:
# If the number is greater than 0, it is positive.
# Otherwise, it is negative.


# Example 5: Password Check

password = "admin123"

if password == "admin123":
    print("Access Granted")
else:
    print("Wrong Password")

# Explanation:
# If the password matches, access is granted.
# Otherwise, an error message is shown.


