# PYTHON LOGICAL OPERATORS FULL CONCEPT

# Logical operators are used to combine conditions

# They return:
# True
# False


# 1. LOGICAL AND OPERATOR (and)

print(" LOGICAL AND OPERATOR (and) ")

# Both conditions must be True

age = 20
salary = 50000

print(age > 18 and salary > 30000)

# True and True = True

# False Example

age = 16
salary = 50000

print(age > 18 and salary > 30000)

# False and True = False


# Another Example

a = 10
b = 5

print(a > 5 and b < 10)

# True and True = True


# Different Data Type Example

num = 10
text = "Hello"

print(num > 5 and text == "Hello")

# True and True = True


# Invalid Example

print("\nInvalid Example:")

try:
    print(10 > "5")

except TypeError:
    print("TypeError: Cannot compare integer and string")


# 2. LOGICAL OR OPERATOR (or)

print("\n LOGICAL OR OPERATOR (or) ")

# At least one condition must be True

age = 16
salary = 50000

print(age > 18 or salary > 30000)

# False or True = True


# Both False Example

age = 15
salary = 10000

print(age > 18 or salary > 30000)

# False or False = False


# Another Example

a = 5
b = 20

print(a > 10 or b > 15)

# False or True = True


# String Example

name = "Ali"

print(name == "Ali" or name == "Ahmed")

# True or False = True


# 3. LOGICAL NOT OPERATOR (not)

print("\n LOGICAL NOT OPERATOR (not) ")

# not changes True into False
# and False into True

print(not True)

print(not False)


# Example

a = 10

print(not a > 5)

# a > 5 = True
# not True = False


# Another Example

age = 15

print(not age >= 18)

# age >= 18 = False
# not False = True


# BOOLEAN CONCEPT

print("\n BOOLEAN CONCEPT ")

print(type(True))
print(type(False))


# SAME DATA TYPE EXAMPLES

print("\n SAME DATA TYPE EXAMPLES ")

print(10 > 5 and 20 > 10)

print(5 < 2 or 10 > 2)

print(not 5 == 5)


# DIFFERENT DATA TYPE EXAMPLES

print("\n DIFFERENT DATA TYPE EXAMPLES ")

print(10 == 10.0)

# int and float
# Python compares values correctly

print("Ali" == "Ali")

# string comparison

print(10 == "10")

# integer and string
# Different data types
# Answer becomes False


# USER LOGIN PROGRAM

print("\n USER LOGIN PROGRAM ")

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")


# ELIGIBILITY PROGRAM

print("\n ELIGIBILITY PROGRAM ")

age = 22
marks = 75

if age >= 18 and marks >= 50:
    print("Eligible")
else:
    print("Not Eligible")


# WEATHER PROGRAM

print("\n WEATHER PROGRAM ")

is_raining = True

if not is_raining:
    print("Go Outside")
else:
    print("Take Umbrella")


# GRADE PROGRAM

print("\n GRADE PROGRAM ")

marks = 45

if marks >= 90:
    print("Grade A")

elif marks >= 50 and marks < 90:
    print("Grade B")

else:
    print("Fail")


# TRUTH TABLE CONCEPT

print("\n TRUTH TABLE ")

print("""
AND Operator

True and True   = True
True and False  = False
False and True  = False
False and False = False


OR Operator

True or True    = True
True or False   = True
False or True   = True
False or False  = False


NOT Operator

not True  = False
not False = True
""")





# LOGICAL OPERATORS TABLE

print("\n===== LOGICAL OPERATORS TABLE =====")

print("""
and   -> Both conditions True
or    -> One condition True
not   -> Reverse result
""")


