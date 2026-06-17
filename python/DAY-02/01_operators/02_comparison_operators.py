
# PYTHON COMPARISON OPERATORS FULL CONCEPT


# Comparison operators compare two values
# and return True or False

# True  = condition is correct
# False = condition is wrong



# 1. EQUAL TO OPERATOR (==)


print("EQUAL TO OPERATOR (==) ")

a = 10
b = 10

print("10 == 10 :", a == b)

# Different values

a = 10
b = 5

print("10 == 5 :", a == b)

# String Example

name1 = "Ali"
name2 = "Ali"

print("Ali == Ali :", name1 == name2)

# Different Data Type

print("10 == '10' :", 10 == "10")

# Concept:
# int and string are different data types
# so answer becomes False



# 2. NOT EQUAL TO OPERATOR (!=)


print("\nNOT EQUAL TO OPERATOR (!=) ")

a = 10
b = 5

print("10 != 5 :", a != b)

# Same value

a = 10
b = 10

print("10 != 10 :", a != b)

# String Example

print("'Ali' != 'Ahmed' :", "Ali" != "Ahmed")



# 3. GREATER THAN OPERATOR (>)


print("\n GREATER THAN OPERATOR (>) ")

a = 20
b = 10

print("20 > 10 :", a > b)

# False Example

print("5 > 10 :", 5 > 10)

# Float Example

print("10.5 > 5 :", 10.5 > 5)



# 4. LESS THAN OPERATOR (<)


print("\nLESS THAN OPERATOR (<) ")

a = 5
b = 10

print("5 < 10 :", a < b)

# False Example

print("20 < 10 :", 20 < 10)

# Float Example

print("2.5 < 10 :", 2.5 < 10)



# 5. GREATER THAN OR EQUAL TO (>=)


print("\nGREATER THAN OR EQUAL TO (>=) ")

a = 10
b = 10

print("10 >= 10 :", a >= b)

# Greater Example

print("20 >= 10 :", 20 >= 10)

# False Example

print("5 >= 10 :", 5 >= 10)



# 6. LESS THAN OR EQUAL TO (<=)


print("\n LESS THAN OR EQUAL TO (<=) ")

a = 5
b = 10

print("5 <= 10 :", a <= b)

# Equal Example

print("10 <= 10 :", 10 <= 10)

# False Example

print("20 <= 10 :", 20 <= 10)



# BOOLEAN CONCEPT


print("\n BOOLEAN CONCEPT ")

# Boolean has only 2 values:
# True
# False

print(type(True))
print(type(False))



# SAME AND DIFFERENT DATA TYPE CONCEPT


print("\nSAME AND DIFFERENT DATA TYPES ")

# Same Data Type

print("5 == 5 :", 5 == 5)

# Different Data Type

print("5 == '5' :", 5 == "5")

# Why False?
# Because integer and string are different



# STRING COMPARISON


print("\n STRING COMPARISON ")

print("'Ali' == 'Ali' :", "Ali" == "Ali")

print("'Ali' == 'ali' :", "Ali" == "ali")

# Capital and small letters are different



# USER AGE CHECK PROGRAM


print("\nAGE CHECK PROGRAM ")

age = 18

print("Age =", age)

print("Age >= 18 :", age >= 18)

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")



# NUMBER CHECK PROGRAM


print("\nNUMBER CHECK PROGRAM ")

num1 = 20
num2 = 15

print("num1 =", num1)
print("num2 =", num2)

if num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greater")



# MARKS CHECK PROGRAM


print("\n MARKS CHECK PROGRAM ")

marks = 75

print("Marks =", marks)

if marks >= 50:
    print("Pass")
else:
    print("Fail")




# COMPARISON OPERATORS TABLE


print("\n COMPARISON OPERATORS TABLE ")

print("""
==  Equal To
!=  Not Equal To
>   Greater Than
<   Less Than
>=  Greater Than Or Equal To
<=  Less Than Or Equal To
""")
