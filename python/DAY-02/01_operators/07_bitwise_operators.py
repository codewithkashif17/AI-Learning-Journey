# PYTHON BITWISE OPERATORS FULL CONCEPT

# Bitwise operators work on binary numbers

# Binary numbers:
# 0 and 1

# Computers understand binary values


# 1. BITWISE AND OPERATOR (&)

print("Bitwise AND Operator &")

a = 5
b = 3

print(a & b)

# Binary:
# 5 = 101
# 3 = 011

# Result:
# 001 = 1


# Another Example

x = 10
y = 7

print(x & y)


# 2. BITWISE OR OPERATOR (|)

print("\nBitwise OR Operator |")

a = 5
b = 3

print(a | b)

# Binary:
# 101
# 011

# Result:
# 111 = 7


# Another Example

x = 10
y = 7

print(x | y)


# 3. BITWISE XOR OPERATOR (^)

print("\nBitwise XOR Operator ^")

a = 5
b = 3

print(a ^ b)

# Binary:
# 101
# 011

# Result:
# 110 = 6


# Another Example

x = 10
y = 7

print(x ^ y)


# 4. BITWISE NOT OPERATOR (~)

print("\nBitwise NOT Operator ~")

a = 5

print(~a)

# Formula:
# ~(n) = -(n + 1)

# ~(5)
# = -(5 + 1)
# = -6


# Another Example

print(~10)


# 5. LEFT SHIFT OPERATOR (<<)

print("\nLeft Shift Operator <<")

a = 5

print(a << 1)

# Binary:
# 101 becomes 1010

# Result = 10


# Another Example

print(5 << 2)

# 101 becomes 10100
# Result = 20


# 6. RIGHT SHIFT OPERATOR (>>)

print("\nRight Shift Operator >>")

a = 20

print(a >> 1)

# Binary shifts right

# Result = 10


# Another Example

print(20 >> 2)

# Result = 5


# BINARY CONCEPT

print("\nBinary Concept")

print(bin(5))

print(bin(10))

print(bin(20))

# bin() converts number into binary


# SAME DATA TYPE EXAMPLES

print("\nSame Data Type Examples")

print(5 & 3)

print(5 | 3)

print(5 ^ 3)


# DIFFERENT DATA TYPE EXAMPLES

print("\nDifferent Data Type Examples")

# Integer and float

try:
    print(5 & 2.5)

except TypeError:
    print("TypeError: Bitwise operators work only with integers")


# Integer and string

try:
    print(5 | "3")

except TypeError:
    print("TypeError: Cannot use bitwise operator with string")


# USER PERMISSION EXAMPLE

print("\nUser Permission Example")

read = 1
write = 2

permission = read | write

print(permission)

# 1 | 2 = 3


# EVEN OR ODD CHECK

print("\nEven Odd Check")

number = 8

if number & 1:
    print("Odd Number")
else:
    print("Even Number")


# MEMORY SHIFT EXAMPLE

print("\nMemory Shift Example")

value = 4

print(value << 1)

print(value << 2)

print(value >> 1)


# BOOLEAN CONCEPT

print("\nBoolean Concept")

print(type(True))

print(type(False))





# BITWISE OPERATORS TABLE

print("\nBitwise Operators Table")

print("""
&    -> AND
|    -> OR
^    -> XOR
~    -> NOT
<<   -> Left Shift
>>   -> Right Shift
""")


# FULL PRACTICE PROGRAM

print("\nFull Practice Program")

a = 6
b = 3

print(a & b)

print(a | b)

print(a ^ b)

print(~a)

print(a << 1)

print(a >> 1)