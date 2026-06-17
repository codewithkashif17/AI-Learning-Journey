# PYTHON IDENTITY OPERATORS FULL CONCEPT

# Identity operators check whether
# two variables point to the same object in memory

# Identity operators:
# is
# is not


# 1. is OPERATOR

print("Identity Operator is")

a = 10
b = 10

print(a is b)

# True
# because both variables point to same object


# String Example

name1 = "Ali"
name2 = "Ali"

print(name1 is name2)

# True


# List Example

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 is list2)

# False
# because both lists are different objects


# Same Object Example

list3 = list1

print(list1 is list3)

# True
# because both variables point to same object


# Float Example

x = 10.5
y = 10.5

print(x is y)


# 2. is not OPERATOR

print("\nIdentity Operator is not")

a = 10
b = 20

print(a is not b)

# True


# String Example

name1 = "Ali"
name2 = "Ahmed"

print(name1 is not name2)

# True


# List Example

list1 = [1, 2]
list2 = [1, 2]

print(list1 is not list2)

# True
# because both are different objects


# Same Object Example

list3 = list1

print(list1 is not list3)

# False


# SAME DATA TYPE EXAMPLES

print("\nSame Data Type Examples")

a = 100
b = 100

print(a is b)

# integer

text1 = "Hello"
text2 = "Hello"

print(text1 is text2)

# string

numbers1 = [1, 2, 3]
numbers2 = [1, 2, 3]

print(numbers1 is numbers2)

# list


# DIFFERENT DATA TYPE EXAMPLES

print("\nDifferent Data Type Examples")

a = 10
b = "10"

print(a is b)

# integer and string are different

x = 10
y = 10.0

print(x is y)

# integer and float are different


# VALUE COMPARISON VS IDENTITY COMPARISON

print("\nValue Comparison vs Identity Comparison")

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(list1 == list2)

# True
# values are same

print(list1 is list2)

# False
# objects are different


# MEMORY CONCEPT

print("\nMemory Concept")

a = [1, 2, 3]

b = a

print(a is b)

# True
# both variables use same memory location


# USER LOGIN CHECK PROGRAM

print("\nUser Login Check Program")

current_user = "admin"

login_user = current_user

if current_user is login_user:
    print("Same User")
else:
    print("Different User")


# NONE CONCEPT

print("\nNone Concept")

data = None

print(data is None)

# True

print(data is not None)

# False


# BOOLEAN CONCEPT

print("\nBoolean Concept")

print(type(True))

print(type(False))





# IDENTITY OPERATORS TABLE

print("\nIdentity Operators Table")

print("""
is       -> Same object
is not   -> Different object
""")


# FULL PRACTICE PROGRAM

print("\nFull Practice Program")

a = [10, 20]

b = [10, 20]

c = a

print(a == b)

# values same

print(a is b)

# different objects

print(a is c)

# same object

print(a is not b)

print(a is not c)