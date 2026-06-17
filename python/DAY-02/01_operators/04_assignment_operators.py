# PYTHON ASSIGNMENT OPERATORS FULL CONCEPT

# Assignment operators are used to assign values to variables


# 1. SIMPLE ASSIGNMENT OPERATOR (=)

print(" SIMPLE ASSIGNMENT OPERATOR (=) ")

a = 10

print("Value of a =", a)

# Concept:
# = stores value into variable


# Integer Example

num = 50

print(num)

# String Example

name = "Ali"

print(name)

# Float Example

price = 99.5

print(price)


# 2. ADD AND ASSIGN OPERATOR (+=)

print("\n ADD AND ASSIGN OPERATOR (+=) ")

a = 10

print("Original Value:", a)

a += 5

print("After += 5 :", a)

# Concept:
# a += 5
# means:
# a = a + 5


# Float Example

price = 50.5

price += 10

print(price)


# String Example

text = "Hello "

text += "World"

print(text)

# String concatenation happens


# Different Data Type Example

print("\nDifferent Data Type Example:")

try:
    num = 10
    text = "5"

    num += text

    print(num)

except TypeError:
    print("TypeError: Cannot add integer and string")


# 3. SUBTRACT AND ASSIGN OPERATOR (-=)

print("\n SUBTRACT AND ASSIGN OPERATOR (-=) ")

a = 20

print("Original Value:", a)

a -= 5

print("After -= 5 :", a)

# Concept:
# a -= 5
# means:
# a = a - 5


# Float Example

price = 100.5

price -= 20

print(price)


# Invalid Example

print("\nInvalid Example:")

try:
    text = "Hello"

    text -= "World"

except TypeError:
    print("TypeError: Subtraction does not work with strings")


# 4. MULTIPLY AND ASSIGN OPERATOR (*=)

print("\n MULTIPLY AND ASSIGN OPERATOR (*=) ")

a = 5

print("Original Value:", a)

a *= 3

print("After *= 3 :", a)

# Concept:
# a *= 3
# means:
# a = a * 3


# Float Example

num = 2.5

num *= 2

print(num)


# String Example

text = "Hi "

text *= 3

print(text)

# String repeats 3 times


# Invalid Example

print("\nInvalid Example:")

try:
    text = "Hello"

    text *= 2.5

except TypeError:
    print("TypeError: String can multiply only with integer")


# 5. DIVIDE AND ASSIGN OPERATOR (/=)

print("\n DIVIDE AND ASSIGN OPERATOR (/=) ")

a = 20

print("Original Value:", a)

a /= 4

print("After /= 4 :", a)

# Concept:
# a /= 4
# means:
# a = a / 4

# Division always returns float


# Float Example

num = 10.5

num /= 2

print(num)


# Division by Zero Example

print("\nDivision By Zero Example:")

try:
    a = 10

    a /= 0

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")


# 6. FLOOR DIVIDE AND ASSIGN OPERATOR (//=)

print("\n FLOOR DIVIDE AND ASSIGN OPERATOR (//=) ")

a = 10

print("Original Value:", a)

a //= 3

print("After //= 3 :", a)

# Concept:
# a //= 3
# means:
# a = a // 3


# Float Example

num = 10.0

num //= 3

print(num)


# 7. MODULUS AND ASSIGN OPERATOR (%=)

print("\n MODULUS AND ASSIGN OPERATOR (%=) ")

a = 10

print("Original Value:", a)

a %= 3

print("After %= 3 :", a)

# Concept:
# a %= 3
# means:
# a = a % 3


# Even/Odd Example

number = 8

number %= 2

print(number)


# 8. EXPONENT AND ASSIGN OPERATOR (**=)

print("\n EXPONENT AND ASSIGN OPERATOR (**=) ")

a = 2

print("Original Value:", a)

a **= 3

print("After **= 3 :", a)

# Concept:
# a **= 3
# means:
# a = a ** 3


# Float Example

num = 2.5

num **= 2

print(num)


# SAME DATA TYPE EXAMPLES

print("\n SAME DATA TYPE EXAMPLES ")

x = 10

x += 5
print(x)

x -= 2
print(x)

x *= 3
print(x)


# DIFFERENT DATA TYPE EXAMPLES

print("\n DIFFERENT DATA TYPE EXAMPLES ")

# int + float

num = 10

num += 2.5

print(num)

# int becomes float automatically


# int + string invalid

try:
    num = 10

    num += "5"

except TypeError:
    print("TypeError: Cannot combine integer and string")


# USER SCORE PROGRAM

print("\n USER SCORE PROGRAM ")

score = 50

print("Original Score:", score)

score += 10

print("After Bonus:", score)

score -= 5

print("After Penalty:", score)


# BANK BALANCE PROGRAM

print("\n BANK BALANCE PROGRAM ")

balance = 1000

print("Original Balance:", balance)

balance += 500

print("After Deposit:", balance)

balance -= 200

print("After Withdraw:", balance)





# ASSIGNMENT OPERATORS TABLE

print("\n ASSIGNMENT OPERATORS TABLE ")

print("""
=    -> Assign
+=   -> Add and assign
-=   -> Subtract and assign
*=   -> Multiply and assign
/=   -> Divide and assign
//=  -> Floor divide and assign
%=   -> Modulus and assign
**=  -> Exponent and assign
""")


