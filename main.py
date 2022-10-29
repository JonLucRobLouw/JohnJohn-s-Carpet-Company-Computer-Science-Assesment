#Jonathan Luc Robertson Louw Carpet company assesment

#Imports all the required modules 

import csv
import os
from typing import Type, final
import decimal
from asyncio import FastChildWatcher
from contextlib import nullcontext
from platform import node
from unicodedata import digit

#This class makes an object for the list of discounts and each object is built from a row in the csv file
#Code refers to the discount code, deduction refers to either the percentage reduced, or the cash deducted based on the type of variable
class discountVoucher:

  def __init__(self, Code, Deduction, Type):

    self.Code = Code
    self.Deduction = Deduction
    self.Type = Type

#Of course, no price is £7.5, it's £7.50 so this function works to ensure that the number is in the right format as a price
def makePriceNum(number):

    numStr = str(number)
    
    if '.' in numStr:
       
       fracStrLi = str(number).split('.')
    
       first = fracStrLi[0]
       last = fracStrLi[1]
    
    
       digits = len(last)
          
       if digits < 2:
       
           print('confirmed')
       
           last = last.replace('0', '')
           last = last + '0' 
    
           numStr = first + '.' + last

    return numStr

#Instead of repeating what is essentially the same core code with every numerical input that involves checking if the data entered is correct and allowing the user to re-inter that data, I have elected to use a function
#This function accepts a parameter of string type, the question actually being asked, other than that everything else is standardised and the final value is simply returned and can then be assigned to any variable that requires said data
#It returns type Boolean. If the user enters yes, it returns True, no is False
def verifyBool(question):

    go = True
    returnData = False

    while go:

        data = input(question)
                
        data = data.lower().strip()

        if data == 'yes' or data == 'no' or data == 'y' or data == 'n':

            if data == 'yes' or data == 'y':

                returnData = True

                go = False
            
            elif data == 'no' or data == 'no':

                returnData = False

                go = False

        else: 

            print('''Ooops didn't quite catch that, please re-inter these values''')
        
    return returnData

#It returns type float. It will make sure the string is casted to a float and make sure the number is definitely numerical before it is casted to prevent crashes
#It will also allow users to re-enter the price if they want or if the input is incorrect
def verifyInt(question):

    #In order to prevent crashes resulting from trying to cast a non-numerical value to a string, the value is only casted to a string type once it has already been confirmed as numerical which is done through the isnumeric inbuilt python function
    
    go = True
    returnData = 0

    while go:

        data = input(question)

        if data.isnumeric():

            #Float instead of int used to allow for decimal values 

            returnData = float(data)

            confirmed = verifyBool('Are you happy with your choice? Type yes to continue, no to re-enter ')

            if confirmed == True:

                go = False

        
        else: 

            print('''Ooops didn't quite catch that, please re-inter these values''')
        
    return returnData

#Accpets 5 parameters. Question is of type string so is inp1 and inp2 but d1 and d2 could be anything. In this code they are only ever strings or Booleans
#inp1 corresponds to d1 and inp2 corresponds with d2. Say we want the user to enter a for inches, b for metres
#inp1 is d1, so if inp1 is a and d1 is inches, if the user enters a as the input, we know the data to output is inches
def verifyMultipleChoice(question, inp1, inp2, d1, d2):

    go = True
    returnData = ''

    while go:

        data = input(question)

        data = data.lower().strip()

        if data == inp1:

            returnData = d1

            go = False
        
        elif data == inp2:

            returnData = d2

            go = False
        
        else:

            print('''Ooops didn't quite catch that, please re-inter these value''')
        
        
    return returnData

print('''Hello, my name is Jonathan with JonJon's  carpet company, what can I do for you?''')
name = input('What is your name? ')

print('Hello', name), 'lets get started!'

#Here we see the verifyMultipleChoice function being used with d1(a), d2(b) inp1(inches), inp2(metres)
measurement = verifyMultipleChoice('Do you want to use inches or metres? Select a for inches and b for metres ', 'a', 'b', 'inches', 'metres')

print('You have selected', measurement)

#Here we see the verifyInt function being used with the question asking about the width and the width of type float being returned and assigned to variable width
width = verifyInt('What is the width of your floor in m? ')
height = verifyInt('What is the height of your floor in m? ')

#The area is calculated by multiplying floats of width and height
area = width * height

#We see the verifyBool function being used with the Boolean return being assigned to addDeductions
addDeductions = verifyBool('Do you have any areas that you do not want to be carpeted, like a piece of furniture? Type yes or no ')

#If the user says yes to having non-carpeted areas addDeductions becomes true and as such the loop begins
while addDeductions == True:

    #Width and height of area to subtract is calculated here 
    width2 = verifyInt('What is the width of the area you want deducted? ')
    height2 = verifyInt('What is the height of the area you want deducted? ')

    deduction = width2 * height2 

    #The deduction couldn't possibly be bigger than the function itself and if they were same the area would be 0
    if deduction >= area:
        
        print('Your deduction is bigger than the total area of your carpet. Please add another entry or exit')

        #The standard verifyMultipleChoice or verifyBool function couldn't be used as there is more than one option esc, yes, no
        #Thererfore the data below is essentially a copy of the verifyMultipleChoice code but with more hen one clause 
        go = True

        while go:
    
            data = input('Type yes to re-enter your deduction, no to continue with no deductions and esc to completely exit ')
    
            data = data.lower().strip()
    
            if data == 'yes':
                
                go = False
            
            elif data == 'no':    
    
                go = False
                addDeductions = False

            elif data == 'esc':

                print('Ending programme')

                os._exit(0)

            else:
    
                print('''Ooops didn't quite catch that, please re-inter these value''')    
    else:

        #Informs the user of the deduction amount and ensures it is casted to a string as floats cannot be printed
        print('''That's a total deduction of''', str(deduction))

        #Returns Bool. If the user enters no, addDeductions will become false and as such the loop will come to a close
        addDeductions = verifyBool('Would you like to add more entries? If you do type yes, to exit type no ')

#Inform the user of the area in square metres
print('''Ok that's an area of', area, 'square metres''') 

#Similar to earlier, due to the presence of multiple clauses the verifyMultipleChoice function is un-useable
carpetType = input('What quality of carpet you want? Select 1 for low quality, 2 for medium quality and 3 for high quality ')

finalPrice = 0

#Multiplies the area with the price depending on the carpet quality
if carpetType == '1':
    finalPrice = area * 3.50
elif carpetType == '2':
    finalPrice = area * 5.50
elif carpetType == '3':
    finalPrice = area * 7.50

#Discount

#Divides total by 10 to get 10 percent and then subtracts that from the total price
deduction = finalPrice / 10

finalPrice -= deduction

print('''It’s your lucky day. Since your new to JonJon's carpet company, we are giving you a discount of 10 percent!''')

deductionStr = makePriceNum(deduction)

print('You save', deductionStr, ' pounds')

isDiscountCode = verifyBool('Do you have an additional discount code? ')

#Discount Codes and gift card data is stored on a separate csv file, a database of sorts

if isDiscountCode == True:

    #This list will be populated by all the available gift codes in the for loop below. Each gift card consists of an object

    discountCodes = []
    
    code = input('Enter your discount code: ')

    #Opens the csv
    with open('discountCodes.csv', newline='') as csvfile:

        #Fetches the data in the csv file

        reader = csv.DictReader(csvfile)

        #Loops over every row, each row being a gift card consisting of the entries Code, Deduction and Type
        #I would advise you refer to the discountCodes.csv file located in this directory for everything to make more sense 

        for row in reader:

            #Appens that csv file as an object to the discountCodes array

         discountCodes.append(discountVoucher(row['Code'], row['Deduction'], row['Type']))

        #Before we have looked over the list, we do not know if the user has found a gift card so by default this variable has been assinged as False 
    
        discountCodeFound = False
        deduction = 0
        deductionFinal = 0.0 

        #Loops through the list to find any matches
        #In retrospect I could have simply found matches within in for row in reader loop. However, I opted for this soltuion to demonstrate how an object can be effectively used within an array
        #I also recognise the deductionFinal variable as necessary as the variable is already a float, so removing this could be an amendment that could possibly improve the efficiency of this code
        #I could imrpove my code by allowing for multiple gift cards

        for i in discountCodes:

            if i.Code == code:

                #If one of the discount codes in the list is equal to the discount code the user entered, we know that the discount code the user entered definitely equates too one of the discount codes in the list
                
                #We assign discountCodeFound as true

                discountCodeFound = True
                
                #One of the attributes of each discount code object is 'Type'
                #Type cash refers to just a linear deduction of amount so if the deduction variable is 20 no matter the total amount 20 pounds is deducted

                if i.Type == 'Cash':

                    deduction = float(i.Deduction)

                    finalPrice -= deduction

                #If on the other hand the type is Percentage, we deduct a percentage of the total amount 
                #So if the deduction amount is 20 we find 20 percent of the total and then deduct said amount from the total 

                else:

                    #Get 1 percent
                    cutter = finalPrice / 100

                    #Mutliply that one percent by the total percentage to be deducted
                    deduction = float(cutter) * float(i.Deduction)

                    deductionFinal = float(deduction)

                    #Subtract that amount from the total
                    finalPrice -= deductionFinal
        
        #If we know they have a discount Code we tell them the amount they save 

        if discountCodeFound == True:

            #Make sure the number is structured in the way a decimal of a price should be (£7.50 not £7.5)
            deductionStr = makePriceNum(deductionFinal)

            print('Your discount code has been applied')
            print('You have saved', deductionStr)

adress = input('Where should we ship your carpet to? ')
phoneNumber = input('What is your phone number so we can keep in contact? ')

finalPriceStr = makePriceNum(finalPrice)

print('Thanks for shopping with the JonJon carpeting company. Your final bill is' , finalPriceStr, 'pounds your carpet will be shipped to', adress)

