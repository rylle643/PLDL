# important_code_and_processes.py

# Hello World
print("Hello, World!")

# Variables
x = 10
y = 5
result = x + y
print(result)

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# For Loop
for i in range(5):
    print(i)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Conditional Statements
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Lists
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Dictionaries
person = {"name": "John", "age": 30}
print(person["name"])

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

john = Person("John", 30)
print(john.greet())

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run.")

# File Handling
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares)

# Modules and Packages
import math
print(math.sqrt(16))

# Creating and using a module
# Save this as mymodule.py
def greet(name):
    return f"Hello, {name}!"

# Using the module
from mymodule import greet
print(greet("Alice"))
