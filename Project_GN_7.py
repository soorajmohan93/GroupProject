'''
File name: Project_GN_7.py
Date created: 25 November 2022
Author: Group 7 - Sooraj Mohan (Student Number: 8842423), Pranav Manikandas

Purpose: 
Group Project Work for IT Automation INFO8025
This python script is a arithemetic calculator to perform operations on two numbers. It can handle divide by zero exceptions and wrong entries from users.
'''
# Functions for arithmetic operations
# Function to Add
def add(first, second):
    return "+", round(first + second,2)

# Function to Subtract
def substract(first, second):
    return "-", round(first-second,2)

# Function to Multiply
def multiply(first, second):
    return "X", round(first * second,2)

# Function to Divide - return Zero Division error exception when divided by zero
def divide(first, second):
    try: 
        return "÷", round(first/second,2)
    except ZeroDivisionError: 
        return None, ZeroDivisionError
    
def TextSpace(width, symbol, text):
    return symbol * ((width - len(text))//2)
    
maxWidth = 60
symbol = "-"
appName = " CALCULATOR APP "

print(f"\n{symbol*maxWidth}")
print("\n{0}{1}{2}".format(TextSpace(maxWidth, "/", appName), appName, TextSpace(maxWidth, "\\", appName)))
print(f"\n{symbol*maxWidth}")

print("\n{0}{1}".format(TextSpace(maxWidth, " ", "Select An Operation"), "Select An Operation"))
print("\n{0}{1}".format(TextSpace(maxWidth, " ", "(1) Add"), "(1) Add"))
print("{0}{1}".format(TextSpace(maxWidth, " ", "(2) Subtract"), "(2) Subtract"))
print("{0}{1}".format(TextSpace(maxWidth, " ", "(3) Multiply"), "(3) Multiply"))
print("{0}{1}".format(TextSpace(maxWidth, " ", "(4) Divide"), "(4) Divide"))
print(f"\n{symbol*maxWidth}")

userChoice = input("\n{0}{1}".format(TextSpace(maxWidth, " ", "Your Choice (1, 2, 3 or 4): "), "Your Choice (1, 2, 3 or 4): "))

try:
    userChoiceInt = int(userChoice)
    if userChoiceInt not in (1,2,3,4):
        raise ValueError()
except ValueError:
    message = "Invalid Input, GoodBye!"
    symbol = "x"
    print(f"\n{symbol*maxWidth}")
    print("\n{0}{1}".format(TextSpace(maxWidth, " ", message), message))
    print(f"\n{symbol*maxWidth}")
    exit()

operationKey = {1:"addition", 2:"subtraction", 3:"multiplication", 4:"division"}
numberCheck = True
while numberCheck:
    try:
        numberText = "Enter first number for {}: ".format(operationKey.get(userChoiceInt))
        firstNumber = float(input("\n{0}{1}".format(TextSpace(maxWidth, " ", numberText), numberText)))
        numberText = "Enter second number for {}: ".format(operationKey.get(userChoiceInt))
        secondNumber = float(input("\n{0}{1}".format(TextSpace(maxWidth, " ", numberText), numberText)))
        numberCheck = False
    except ValueError:
        print("The program is expecting two numeric values! Please Try Again with Whole or decimal numbers.")
del operationKey

print(f"\n{symbol*maxWidth}")
if userChoiceInt == 1:
    operation, result = add(firstNumber, secondNumber)
elif userChoiceInt == 2:
    operation, result = substract(firstNumber,secondNumber)
elif userChoiceInt == 3:
    operation, result = multiply(firstNumber,secondNumber)
elif userChoiceInt == 4:
    operation, result = divide(firstNumber, secondNumber)
    
if result == ZeroDivisionError:
    resultText = "Exception Occurred: Cannot Divide By Zero!"
else:
    resultText = "Here is your result: {0} {1} {2} = {3}".format(round(firstNumber,2), operation, round(secondNumber,2), result)
    
print("\n{0}{1}".format(TextSpace(maxWidth, " ", resultText), resultText))
print(f"\n{symbol*maxWidth}")
    
thankMessage = " THANK YOU FOR USING CALCULATOR APP "
print("\n{0}{1}{2}".format(TextSpace(maxWidth, "/", thankMessage), thankMessage, TextSpace(maxWidth, "\\", thankMessage)))
print(f"\n{symbol*maxWidth}")
