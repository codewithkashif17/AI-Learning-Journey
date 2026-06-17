
# PYTHON ARITHMETIC OPERATORS FULL CONCEPT



# 1. ADDITION OPERATOR (+)


print("===== ADDITION OPERATOR =====")

# Same Data Type (int + int)

a = 10
b = 5

result = a + b

print("10 + 5 =", result)

# Different Data Type (int + float)

a = 10
b = 2.5

result = a + b

print("10 + 2.5 =", result)

# String Addition (Concatenation)

first_name = "Ali "
last_name = "Khan"

print(first_name + last_name)

# Invalid Example

print("\nInvalid Example:")

try:
    a = 10
    b = "5"

    print(a + b)

except TypeError:
    print("TypeError: Cannot add integer and string directly")

# Correct Way

a = 10
b = "5"

print("Correct Answer:", a + int(b))



# 2. SUBTRACTION OPERATOR (-)


print("\n===== SUBTRACTION OPERATOR =====")

a = 20
b = 5

print("20 - 5 =", a - b)

# Different Data Type

a = 20
b = 2.5

print("20 - 2.5 =", a - b)

# Invalid Example

print("\nInvalid Example:")

try:
    a = "20"
    b = 5

    print(a - b)

except TypeError:
    print("TypeError: Subtraction only works with numbers")



# 3. MULTIPLICATION OPERATOR (*)


print("\n===== MULTIPLICATION OPERATOR =====")

a = 4
b = 5

print("4 * 5 =", a * b)

# Float Example

a = 4
b = 2.5

print("4 * 2.5 =", a * b)

# String Multiplication

text = "Hello "

print(text * 3)

# Invalid Example

print("\nInvalid Example:")

try:
    print("Hello" * 2.5)

except TypeError:
    print("TypeError: String can only multiply with integer")



# 4. DIVISION OPERATOR (/)


print("\n===== DIVISION OPERATOR =====")

a = 10
b = 2

print("10 / 2 =", a / b)

# Float Result

a = 10
b = 4

print("10 / 4 =", a / b)

# Division by Zero

print("\nDivision By Zero Example:")

try:
    a = 10
    b = 0

    print(a / b)

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero")



# 5. FLOOR DIVISION OPERATOR (//)


print("\n===== FLOOR DIVISION OPERATOR =====")

a = 10
b = 3

print("10 // 3 =", a // b)

# Float Example

print("10.0 // 3 =", 10.0 // 3)



# 6. MODULUS OPERATOR (%)


print("\n===== MODULUS OPERATOR =====")

a = 10
b = 3

print("10 % 3 =", a % b)

# Even/Odd Program

number = 8

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")



# 7. EXPONENT OPERATOR (**)


print("\n===== EXPONENT OPERATOR =====")

print("2 ** 3 =", 2 ** 3)

print("2.5 ** 2 =", 2.5 ** 2)



# FULL PRACTICE PROGRAM


print("\n===== FULL PRACTICE PROGRAM =====")

num1 = 15
num2 = 4

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)
print("Floor Division =", num1 // num2)
print("Modulus =", num1 % num2)
print("Exponent =", num1 ** num2)





