# 01 IF-STATEMENT

## What is an If Statement?

An if statement is used to check a condition in Python.

- If the condition is **True**, the code runs.
- If the condition is **False**, the code is skipped.
Example 1: Basic If Statement
age = 18

if age >= 18:
    print("You are eligible for voting")
## Explanation:
The condition checks if age is greater than or equal to 18.
Since the condition is True, the message is printed.

## Example 1:
### Basic If Statement

```python
age = 18

if age >= 18:
    print("You are eligible for voting")

```

## Explanation:
The condition checks if age is greater than or equal to 18.
Since the condition is True, the message is printed.

## Example 2:
###  Positive Number Check
number = 10
```python
if number > 0:
    print("Number is positive")

 ```   
## Explanation:
The condition checks if the number is greater than **0**.
If **True**, it prints that the number is positive.

## Example 3:
### Password Verification

```python
password = "python123"

if password == "python123":
    print("Login Successful")

```
## Explanation:

**==** is used to compare two values.
If both values are equal, the condition becomes **True**.

## Example 4:
### Even Number Check

```python
num = 8

if num % 2 == 0:
    print("Even Number")

```
## Explanation:

**%** gives the remainder.
If remainder is **0**, the number is **even**.

Example 5: Pass or Fail Check
marks = 75

if marks >= 50:
    print("Pass")
Explanation:
If marks are 50 or greater, the student passes.


# 02 IF-ELSE STATEMENTS

## What is an If Else Statement?

The **if else** statement is used to make decisions in Python.

If the condition is **True**, the if block runs.
Otherwise, the else block runs.

## Example 1: Age Check

```python
age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

```

## Explanation:
If age is 18 or more, the first message prints.
Otherwise, the second message prints.

## Example 2:

### Even or Odd Number

```python
number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

## Explanation:
If remainder is 0, the number is even.
Otherwise, the number is odd.

## Example 3:
### Pass or Fail

```python 
marks = 40

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

## Explanation:
If marks are 50 or greater → Pass
Otherwise → Fail

## Example 4:
### Positive or Negative Number

```python
num = -5

if num > 0:
    print("Positive Number")
else:
    print("Negative Number")

```

## Explanation:
If number is greater than 0 → Positive
Otherwise → Negative

## Example 5:
### Password Check

```python
password = "admin123"

if password == "admin123":
    print("Access Granted")
else:
    print("Wrong Password")

```


## Explanation:
If password matches → Access Granted
Otherwise → Wrong Password