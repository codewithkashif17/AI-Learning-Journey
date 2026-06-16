# Day 01 - Python Basics (Complete Notes)

Welcome to my Python learning journey.  
This file contains all Day 01 topics with explanation + code.

---

# Python Introduction

Python is a high-level programming language used for:

- Web Development (Django, Flask)
- Software Development
- Data Science (NumPy, Pandas)
- Artificial Intelligence (TensorFlow)
- Machine Learning (Scikit-learn, Keras)
- Game Development (Pygame)

---

# 📄 1. hello.py (First Program)

## Concept:
This is the first program in Python. It prints output on screen.

```python
# Python: Programming language

# Used for:
# web development, software development, data science,
# AI, machine learning, game development

print("hello world")
print("hello today my 1st day of starting python learning")

```

# 📄 2. variables.py

## Concept: Variables

Variables are containers used to store data values in memory.  
They allow us to store and reuse data in our program.

---

# 💡 Why Variables are used?

- To store data values
- To perform operations on data
- To make programs dynamic and reusable

---

# ⚙️ Memory Concept

Variables are stored in computer memory (RAM) during program execution.

---

# Rules for Naming Variables

1. A variable name must start with a letter or underscore (_)
2. A variable name cannot start with a number
3. A variable can only contain letters, numbers, and underscore (_)
4. Variable names are case-sensitive
5. A variable cannot be a Python keyword
6. A variable name should be meaningful
7. A variable name should be short and descriptive

---

#  Important Note

Variable names are case-sensitive:

```python
name = "kashif"
Name = "kashif"
```

# 3. input_output.py 

# 📄 Input and Output in Python

##  Concept: Input & Output

Input and output are used to take data from the user and display results.

This helps us interact with users in a program.

---

# 💡 Why Input/Output is important?

- To get user data
- To display results
- To make interactive programs

---

# ⚙️ Data Type Input Methods

- `int(input())` → Integer input
- `float(input())` → Decimal input
- `str(input())` → String input (default)
- `bool(input())` → Boolean input
- `complex(input())` → Complex number input

---

# 🧾 Example Code

```python id="io12345"
# Python Input and Output

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
```

# 4. comments.py

# 📄 Comments in Python

## Concept: Comments

Comments are used to explain the code.  
They help developers understand the program easily.

👉 Comments are ignored by the Python interpreter, so they do not affect the output.

---

# 💡 Why Comments are important?

- To explain code logic
- To make code readable
- To help other developers understand your code

---

# 🧾 Types of Comments in Python

## 1. Single Line Comment
Starts with `#`

## 2. Multi Line Comment
Starts and ends with triple quotes `""" """`

---

# 🧾 Example Code

```python id="comment01"
# comments: comments are used to explain code.
# comments are ignored by python interpreter.
# comments can be single line or multi line
# single line comment starts with #
# multi line comment starts with """

print("hello world")

```

# 5. data_types.py

# 📄 Data Types in Python

## Concept: Data Types

Data types define the type of value stored in a variable.  
They help Python understand what kind of data is being used.

---

# 💡 Why Data Types are important?

- To identify type of data
- To perform correct operations
- To avoid errors in programs

---

# Common Data Types in Python

1. **String (`str`)** → Text data  
   Example: `"kashif"`

2. **Integer (`int`)** → Whole numbers  
   Example: `20`

3. **Float (`float`)** → Decimal numbers  
   Example: `20.5`

4. **Boolean (`bool`)** → True or False  
   Example: `True`, `False`

5. **Complex (`complex`)** → Complex numbers  
   Example: `2+3j`

---

# 🧾 Example Code

```python id="dt001"
# Data types examples

name = "kashif"       # string
age = 20              # integer
is_married = False    # boolean
address = "kamal khel kohat"  # string

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(is_married)) # <class 'bool'>
print(type(address))    # <class 'str'>