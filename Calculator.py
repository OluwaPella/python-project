#!/usr/bin/python3
import math
def display_option():
    print("Select an option:")
    print("1. Addition opertion")
    print("2. Subtract opertion")
    print("3. Multiply opertion")
    print("4. Divide opertion")
    print("5. squreroot opertion")
    print("6. exponentiation opertion")
    print("7. logarithm operations operation")
    print("8.  trigonometric operations")
    print("0. Go back to the main options")
def process_option(option):
    if option == "1": #perform addtion of numbers
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        valid = True
        try:
            num1 = int(num1)
        except ValueError:
            print("Invalid input for num1")
            valid = False
        try:
            num2 = int(num2)
        except ValueError:
            print("Invalid input for num2")
            valid = False
        if valid:
            print("Sum: {} + {} = {}".format(num1, num2, num1 + num2))
        else:
            print("Please enter a valid integer")
    elif option == "2": #perform subtraction of numbers
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        valid = True
        try:
            num1 = int(num1)
        except ValueError:
            print("Invalid input for num1")
            valid = False
        try:
            num2 = int(num2)
        except ValueError:
            print("Invalid input for num2")
            valid = False
        if valid:
            print("Sum: {} - {} = {}".format(num1, num2, num1 - num2))
        else:
            print("Please enter a valid integer")
    elif option == "3": # perform multiplication of numbers
        num1 = input("Enter the first number: ")
        #take users input for first input
        num2 = input("Enter the second number: ")
        # #take users input for first input
        valid = True
        try:
            num1 = int(num1)
        except ValueError:
            print("Invalid input for num1")
            valid = False
        try:
            num2 = int(num2)
        except ValueError:
            print("Invalid input for num2")
            valid = False
        if valid:
            print("multiplication: {} * {} = {}".format(num1, num2, num1 * num2))
        else:
            print("Please enter a valid integer")
    elif option == "4": #perform division of numbers
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        valid = True
        try:
            num1 = int(num1)
        except ValueError:
            print("Invalid input for num1")
            valid = False
        try:
            num2 = int(num2)
        except ValueError:
            print("Invalid input for num2")
            valid = False
    if valid:
            print("result: {} - {} = {}".format(num1, num2, num1 / num2))
    else:
            print("Please enter a valid integer")
    if option == "5":
        num1 = input("Enter a number: ")
        num1 = int(num1)
        print("Square root of %f " % (math.sqrt(num1)))
    if option == "6":
        num1 = input("Enter a number: ")
        num1 = int(num1)
        print("result %f " % (math.exp(num1)))
    if option == "7":
        num1 = input("Enter a number: ")
        num1 = int(num1)
        print("result %f " % (math.log(num1)))
    if option == "8":
        return True
    elif option == "0":
        return False
    else:
        print("Invalid input")

while True:
    display_option()
    operation = input("Enter your choice: ")
    if not process_option(operation):
        break

