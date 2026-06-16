#python Input and Output:
#input and output are used to take input from user and print output to user
#for interacting with user we use input and output
#for integer input we use int(input())
# for float input we use float(input())
# for string input we use input()
# for boolean input we use bool(input())
# for complex input we use complex(input())

name = input("Enter your name: ")
print("Hello " + name)

age = int(input("Enter your age: "))
print("You are " + str(age) + " years old")

height = float(input("Enter your height: "))
print("You are " + str(height) + " meters tall")

is_married = bool(input("Are you married? (True or False): "))
print("You are married: " + str(is_married))

complex_number = complex(input("Enter a complex number: "))
print("The complex number is: " + str(complex_number))