<#################################################################################################################
File name: Project_GN_7.ps1
Date created: 25 November 2022
Author: Group 7 - Sooraj Mohan (Student Number: 8842423) and Pranav Manikanda das (Student Number: 8782064)

Purpose: 
Group Project Work for IT Automation INFO8025
This powershell script is an arithemetic calculator to perform operations on two numbers. 
It can handle divide by zero exceptions and wrong entries from user
#################################################################################################################>


# Functions for arithmetic operations
# Function to Add
function Addition([decimal]$firstNumber, [decimal]$secondNumber){
    return $firstNumber + $secondNumber
}

# Function to Subtract
function Subtraction([decimal]$firstNumber, [decimal]$secondNumber){
    return $firstNumber - $secondNumber
}

# Function to Multiply
function Multiplication([decimal]$firstNumber, [decimal]$secondNumber){
    return $firstNumber * $secondNumber
}

# Function to Divide - return Zero Division error string message when divided by zero
function Division([decimal]$firstNumber, [decimal]$secondNumber){
    try{
        return $firstNumber / $secondNumber
    }
    catch {
        return "`r`n                             Exception Occurred: Cannot Divide By Zero!"
    }
}

# Welcome message displaying for user which shows the various arithemetic operations available
Write-Host "----------------------------------------------------------------------------------------------------"
Write-Host "////////////////////////////////////////// CALCULATOR APP \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
Write-Host "----------------------------------------------------------------------------------------------------`r`n"
Write-Host "                                        Select An Operation"
Write-Host "                                              (1) Add"
Write-Host "                                            (2) Subtract"
Write-Host "                                            (3) Multiply"
Write-Host "                                             (4) Divide`r`n"
Write-Host "----------------------------------------------------------------------------------------------------`r`n"

# Take user input into a string variable
$userInput = Read-Host -Prompt "                                    Your Choice (1, 2, 3 or 4)"

<# Type cast string variable which contains user input into string. Exception is raised if user enters 
non numeric character or outside the given range 1 to 4 #>
try{
    $userInputInt = [int]$userInput
    if ($userInputInt -lt 1 -or $userInputInt -gt 4){
        throw 
    }
}
# if exception is raised then its caught and exits the execution after the message display
catch{
    Write-Host "`r`nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    Write-Host "                                      Invalid Input, GoodBye!"
    Write-Host "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`r`n"
    exit
}

# A hashtable variable to hold the operation name corresponding to the user entry - will be used to display message to user
$operationKey = @{
                1 = 'addition'
                2 = 'subtraction'
                3 = 'multiplication'
                4 = 'division'
            }

# Display to confirm user's selection
Write-Host "`r`n                                        You chose $($operationKey.$userInputInt)"

#  taking user's input and type casting to float. If user enters an invalid number, the script asks user to input values again.
do{
    try{
        Write-Host "`r`n----------------------------------------------------------------------------------------------------"
        [float]$firstOperand = Read-Host -Prompt "`r`n                                 Enter first number for $($operationKey.$userInputInt)"
        [float]$secondOperand = Read-Host -Prompt "`r`n                                 Enter second number for $($operationKey.$userInputInt)"
        Write-Host "`r`n----------------------------------------------------------------------------------------------------"
        break # break from loop when valid values are entered
    }
    catch{
        Write-Host "`r`n    The program is expecting two numeric values! Please Try Again with Whole or decimal numbers."
    }

}while($true) # keep looping until break is encountered

# The hashtable is cleared and values for the keys are updated with operation symbols - will be used to display the result
$operationKey.Clear()
$operationKey = @{
    1 = '+'
    2 = '-'
    3 = 'X'
    4 = '÷'
}

# Check the user input and call the appropriate function. The resulting value is assigned to $result variable
if ($userInputInt -eq 1){
    $result = Addition -firstNumber $firstOperand -secondNumber $secondOperand
}
elseif ($userInputInt -eq 2){
    $result = Subtraction -firstNumber $firstOperand -secondNumber $secondOperand
}
elseif ($userInputInt -eq 3){
    $result = Multiplication -firstNumber $firstOperand -secondNumber $secondOperand
}
elseif ($userInputInt -eq 4){
    $result = Division -firstNumber $firstOperand -secondNumber $secondOperand
}

<# For divide by zero exception, the results will be a string. So, display only the text in the result variable, 
else the result of operation is displayed #>
if ($result.GetType().Name -eq "String"){
    Write-Host $result
}
else{
    Write-Host "`r`n                                Here is your result: $([math]::Round($firstOperand,2)) $($operationKey.$userInputInt) $([math]::Round($secondOperand,2)) = $([math]::Round($result,2))"
    
}
$operationKey.Clear() # Clearing hash table

# Closing message for script
Write-Host "`r`n----------------------------------------------------------------------------------------------------"
Write-Host "//////////////////////////////// THANK YOU FOR USING CALCULATOR APP \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"
Write-Host "----------------------------------------------------------------------------------------------------"


