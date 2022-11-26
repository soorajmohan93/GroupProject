
# Functions for arithmetic operations
# Function to Add
def add(first, second):
    return f"Here is the result: {first} + {second} = {round(first + second,2)}"

# Function to Subtract
def substract(first, second):
    return f"Here is the result: {first} - {second} = {round(first-second,2)}"

# Function to Multiply
def multiply(first, second):
    return f"Here is the result: {first} X {second} = {round(first * second,2)}"

# Function to Divide - return Zero Division error exception when divided by zero
def divide(first, second):
    try: 
        return f"Here is the result: {first} / {second} = {round(first/second,2)}"
    except ZeroDivisionError: 
        return ZeroDivisionError("Cannot Divide by Zero!")
    


print("\n------------------------------------------------------\n--------------------- CALCULATOR APP -----------------\n------------------------------------------------------\n")
userChoice = input("Select An Operation\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n\nYour Choice (1, 2, 3 or 4): ")

try:
    userChoiceInt = int(userChoice)
    if userChoiceInt not in (1,2,3,4):
        raise ValueError()
except ValueError:
    print("Invalid Input, GoodBye")
    exit()

numberCheck = True
while numberCheck:
    try:
        firstNumber = float(input("Enter first number: "))
        secondNumber = float(input("Enter second number: "))
        numberCheck = False
    except ValueError:
        print("The program is expecting two numeric values!")

if userChoiceInt == 1:
    print(add(firstNumber,secondNumber))
elif userChoiceInt == 2:
    print(substract(firstNumber,secondNumber))
elif userChoiceInt == 3:
    print(multiply(firstNumber,secondNumber))
elif userChoiceInt == 4:
    print(divide(firstNumber, secondNumber))


