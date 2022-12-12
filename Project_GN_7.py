##############################################################################################################################
# File name: Project_GN_7.py
# Date created: 25 November 2022
# Author: Group 7 - Sooraj Mohan (Student Number: 8842423) and Pranav Manikanda das (Student Number: 8782064)

# Purpose: 
# Group Project Work for IT Automation INFO8025
# This python script is a arithemetic calculator to perform operations on two numbers. 
# It can handle divide by zero exceptions and wrong entries from user
##############################################################################################################################

# Functions for arithmetic operations
# Function to Add
def Add(first, second):
    return "+", round(first + second, 2)

# Function to Subtract
def Subtract(first, second):
    return "-", round(first-second, 2)

# Function to Multiply
def Multiply(first, second):
    return "X", round(first * second, 2)

# Function to Divide - return Zero Division error exception when divided by zero
def Divide(first, second):
    try: 
        return "÷", round(first/second ,2)
    except ZeroDivisionError: 
        return None, ZeroDivisionError

# Function to centre the text messages in Calculator - it can add symbols before and after text
def TextSpace(width, startSymbol, endSymbol, text):
    numberOfSpace = ((width - len(text)) // 2)
    return startSymbol*numberOfSpace + text + endSymbol * numberOfSpace

# Execution starts here
if __name__ == '__main__':
    # maximum width displayed is 100 characters
    maxWidth = 100
    symbol = "-"
    appName = " THE CALCULATOR APP " 

    # This prints a separation with the symbol character times the maximum width
    print(f"\n{symbol * maxWidth}")
    # App welcome message
    print("\n{0}".format(TextSpace(maxWidth, "/", "\\", appName)))
    print(f"\n{symbol * maxWidth}")

    # Menu with list of operators
    print("\n{0}".format(TextSpace(maxWidth, " ", "", "Select An Operation")))
    print("\n{0}".format(TextSpace(maxWidth, " ", "", "(1) Add")))
    print("{0}".format(TextSpace(maxWidth, " ", "", "(2) Subtract")))
    print("{0}".format(TextSpace(maxWidth, " ", "", "(3) Multiply")))
    print("{0}".format(TextSpace(maxWidth, " ", "", "(4) Divide")))
    print(f"\n{symbol * maxWidth}")

    # Prompt for user input
    userChoice = input("\n{0}".format(TextSpace(maxWidth, " ", "", "Your Choice (1, 2, 3 or 4): ")))

    # if user input is invalid - any other value than 1,2,3 or 4 then message is displayed and execution terminated
    try:
        userChoiceInt = int(userChoice)
        if userChoiceInt not in (1,2,3,4):
            raise ValueError() # raise error incase of integer values outside 1-4
    except ValueError:
        message = "Invalid Input, GoodBye!"
        symbol = "x"
        print(f"\n{symbol*maxWidth}")
        print("\n{0}".format(TextSpace(maxWidth, " ", "", message)))
        print(f"\n{symbol*maxWidth}")
        exit() # terminate execution

    # dictionary variable that maps value to operation - the operation name will be printed for user
    operationKey = {1:"addition", 2:"subtraction", 3:"multiplication", 4:"division"}
    
    # Display to confirm user's selection
    print("\n{0}".format(TextSpace(maxWidth, " ", "", "You chose {0} operation!".format(operationKey.get(userChoiceInt)))))
    print(f"\n{symbol*maxWidth}")
    
    # While loop used for looping until both valid values are entered
    while True:
        try:
            # prompt for first number
            numberText = "Enter first number for {}: ".format(operationKey.get(userChoiceInt))
            firstNumber = float(input("\n{0}".format(TextSpace(maxWidth, " ", "", numberText))))
            
            # prompt for second number
            numberText = "Enter second number for {}: ".format(operationKey.get(userChoiceInt))
            secondNumber = float(input("\n{0}".format(TextSpace(maxWidth, " ", "", numberText))))
            break # if both are valid numbers then exit loop
        except ValueError:
            message = "The program is expecting two numeric values! Please Try Again with Whole or decimal numbers."
            print("\n{0}".format(TextSpace(maxWidth, " ", "", message)))
    
    del operationKey # dictonary variable no longer used, hence clear it

    # conditions to check input for operation and calling the appropriate function to operate
    print(f"\n{symbol*maxWidth}")
    if userChoiceInt == 1:
        operation, result = Add(firstNumber, secondNumber)
    elif userChoiceInt == 2:
        operation, result = Subtract(firstNumber,secondNumber)
    elif userChoiceInt == 3:
        operation, result = Multiply(firstNumber,secondNumber)
    elif userChoiceInt == 4:
        operation, result = Divide(firstNumber, secondNumber)
    
    # if divide function return divide by zero exception then print Cannot divide by zero message on console and exit  
    if result == ZeroDivisionError:
        resultText = "Exception Occurred: Cannot Divide By Zero!"
    # else show the operands, operation and result of operation
    else:
        resultText = "Here is your result: {0} {1} {2} = {3}".format(round(firstNumber,2), operation, round(secondNumber,2), result)
    # The result text is centre aligned 
    print("\n{0}".format(TextSpace(maxWidth, " ", "", resultText)))
    print(f"\n{symbol*maxWidth}")
    # End execution with Thanks!
    thankMessage = " THANK YOU FOR USING THE CALCULATOR APP "
    print("\n{0}".format(TextSpace(maxWidth, "/", "\\", thankMessage)))
    print(f"\n{symbol*maxWidth}")