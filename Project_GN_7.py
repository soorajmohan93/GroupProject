'''
File name: Project_GN_7.py
Date created: 25 November 2022
Author: Group 7 - Sooraj Mohan (Student Number: 8842423), Pranav Manikandas

Purpose: 
Group Project Work for IT Automation INFO8025
This python script is a arithemetic calculator to perform operations on two numbers. It can handle divide by zero exceptions/
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
    

    
dashSeparator = "-" * 50
appName = " CALCULATOR APP "
appNameSpace = "-" *((len(dashSeparator) - len(appName))//2)

print(f"\n{dashSeparator}")
print("\n{0}{1}{2}".format(appNameSpace, appName, appNameSpace))
print(f"\n{dashSeparator}")

userChoice = input("Select An Operation\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n\nYour Choice (1, 2, 3 or 4): ")

try:
    userChoiceInt = int(userChoice)
    if userChoiceInt not in (1,2,3,4):
        raise ValueError()
except ValueError:
    message = "Invalid Input, GoodBye"
    messageSpace = " " *((len(dashSeparator) - len(message))//2)
    print(f"\n{dashSeparator}")
    print("\n{0}{1}{2}".format(messageSpace, message, messageSpace))
    print(f"\n{dashSeparator}")
    exit()

numberCheck = True
while numberCheck:
    try:
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))
        numberCheck = False
    except ValueError:
        print("The program is expecting two numeric values! Please Try Again with Whole or decimal numbers.")

print(f"\n{dashSeparator}")
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
    
resultTextSpace = " " *((len(dashSeparator) - len(resultText))//2)
print("\n{0}{1}{2}".format(resultTextSpace, resultText, resultTextSpace))

print(f"\n{dashSeparator}")
thankMessage = " THANK YOU FOR USING CALCULATOR APP "
thankMessageSpace = "-" *((len(dashSeparator) - len(thankMessage))//2)
print("\n{0}{1}{2}".format(thankMessageSpace, thankMessage, thankMessageSpace))
