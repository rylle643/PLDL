def inandout():

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    current_year = 2024
    year_turn_100 = current_year + (100 - age)
    print(f"{name}, you will turn 100 in the year {year_turn_100}.")



def pandn():
    number = float(input("Enter a number: "))
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")



def mtable():
    number = float(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")



def ltos():
    numbers = []
    for i in range(5):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    largest = max(numbers)
    smallest = min(numbers)
    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")



def is_even(num):
    return num % 2 == 0
number = int(input("Enter a number: "))
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")



def fact():
    number = int(input("Enter a number to calculate its factorial: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"The factorial of {number} is: {factorial}")



def palindromes():
    word = input("Enter a word: ")
    if word == word[::-1]:
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")



def file():
    filename = input("Enter the filename: ")
    with open(filename, "w") as file:
        file.write("Hello, World!")
    with open(filename, "r") as file:
        content = file.read()
        print(f"Content of the file: {content}")



def calc():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operator."
    print(f"The result is: {result}")



def split():
    sentence = input("Enter a sentence: ")
    word_list = sentence.split()
    frequency = {}
    for word in word_list:
        word = word.lower()
        frequency[word] = frequency.get(word, 0) + 1
    for word, count in frequency.items():
        print(f"{word}: {count}")

    def primes():
        number = int(input("Enter a number: "))
        if number <= 1:
            print(f"{number} is not a prime number.")
        else:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    print(f"{number} is not a prime number.")
                    break
            else:
                print(f"{number} is a prime number.")

def fizz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
