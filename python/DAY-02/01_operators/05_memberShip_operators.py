# PYTHON MEMBERSHIP OPERATORS FULL CONCEPT

# Membership operators are used to check
# if a value exists inside a sequence

# Sequence examples:
# String
# List
# Tuple


# 1. in OPERATOR

print("Membership Operator in")

# String Example

text = "Hello World"

print("Hello" in text)

# True
# because "Hello" exists in text

print("Python" in text)

# False
# because "Python" does not exist


# List Example

numbers = [10, 20, 30, 40]

print(20 in numbers)

# True

print(100 in numbers)

# False


# Tuple Example

data = (1, 2, 3, 4)

print(3 in data)

print(10 in data)


# Character Checking

name = "Ali"

print("A" in name)

print("z" in name)


# Integer Example

values = [1, 2, 3, 4, 5]

print(5 in values)

print(8 in values)


# Float Example

prices = [10.5, 20.5, 30.5]

print(20.5 in prices)

print(50.5 in prices)


# Different Data Type Example

print("\nDifferent Data Type Examples")

print(10 in [10, 20, 30])

# integer inside integer list

print("10" in ["10", "20", "30"])

# string inside string list

print(10 in ["10", "20", "30"])

# integer and string are different
# answer becomes False


# 2. not in OPERATOR

print("\nMembership Operator not in")

# String Example

text = "Python Programming"

print("Java" not in text)

# True

print("Python" not in text)

# False


# List Example

numbers = [1, 2, 3, 4, 5]

print(10 not in numbers)

print(2 not in numbers)


# Tuple Example

data = ("Ali", "Ahmed", "Sara")

print("Zara" not in data)

print("Ali" not in data)


# USER LOGIN CHECK PROGRAM

print("\nUser Login Check Program")

users = ["Ali", "Ahmed", "Sara"]

username = "Ali"

if username in users:
    print("User Found")
else:
    print("User Not Found")


# BANNED WORD CHECK PROGRAM

print("\nBanned Word Check Program")

message = "This is a bad word"

if "bad" in message:
    print("Warning: Banned word detected")
else:
    print("Message is clean")


# SUBJECT CHECK PROGRAM

print("\nSubject Check Program")

subjects = ["Math", "English", "Science"]

if "Math" in subjects:
    print("Math Subject Available")

if "Biology" not in subjects:
    print("Biology Subject Not Available")


# SAME DATA TYPE EXAMPLES

print("\nSame Data Type Examples")

print("Ali" in ["Ali", "Ahmed"])

print(5 in [1, 2, 3, 4, 5])

print(2.5 in [1.5, 2.5, 3.5])


# DIFFERENT DATA TYPE EXAMPLES

print("\nDifferent Data Type Examples")

print(5 in ["5", "10"])

# integer and string are different

print("5" in ["5", "10"])

# correct string comparison

print(2.5 in [2, 3, 4])

# float and integer values are different


# BOOLEAN CONCEPT

print("\nBoolean Concept")

print(type(True))

print(type(False))





# MEMBERSHIP OPERATORS TABLE

print("\nMembership Operators Table")

print("""
in       -> Value exists
not in   -> Value does not exist
""")


# FULL PRACTICE PROGRAM

print("\nFull Practice Program")

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)

print("Orange" in fruits)

print("Banana" not in fruits)

print("Orange" not in fruits)