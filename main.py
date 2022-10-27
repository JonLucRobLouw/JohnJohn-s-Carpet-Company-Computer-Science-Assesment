#Jonathan Luc Robertson Louw Carpet company assesment

import csv
import os
from typing import Type, final
import decimal
from asyncio import FastChildWatcher
from contextlib import nullcontext
from platform import node
from unicodedata import digit

class discountVoucher:

  def __init__(self, Code, Deduction, Type):

    self.Code = Code
    self.Deduction = Deduction
    self.Type = Type

#Instead of repeating what is essentailly the same core code with every numerical input that involves checking if the data entered is correct and allowing the user to re-inter that data, I have elected to use a function
#This function accepts a paramter of string type, the question actually being asked, other then that evyerthing else is standarised and the final value is simply returned and can then be assinged to any variable that requires said data

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

            print('Ooops dont quite catch that, please re-inter these values')
        
    return returnData

def verifyInt(question):

    #In order to prevent crashes resluting from trying to cast a non numerical value to a string, the value is only casted to a string type once it has already been confiremd as numerical which is done through the isnumeric inbuilt python function
    
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

            print('Ooops dont quite catch that, please re-inter these values')
        
    return returnData


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

            print('Ooops dont quite catch that, please re-inter these value')
        
        
    return returnData


print('''Hello, my name is Jonathan with JonJon's  carpet company, what can I do for you?''')
name = input('What is your name? ')

print('Hello', name), 'lets get started!'

measurement = verifyMultipleChoice('Do you want to use inches or metres? Select a for inches and b for metres ', 'a', 'b', 'inches', 'metres')


width = verifyInt('What is the width of your floor in m? ')
height = verifyInt('What is the height of your floor in m? ')

area = width * height

addDeductions = verifyBool('Do you have any areas that you do not want to be carpeted, like a piece of funiture? Type yes or no ')

while addDeductions == True:

    width2 = verifyInt('What is the width of the area you want deducted? ')
    height2 = verifyInt('What is the height of the area you want deducted? ')

    deduction = width2 * height2 

    if deduction >= area:
        
        print('Your deduction is bigger then the total area of your carpet. Please add another entry or exit')

        go = True

        while go:
    
            data = input('Type yes to re-enter your deduction, no to continue with no deductions and esc to completley exit ')
    
            data = data.lower().strip()
    
            if data == 'yes':
                
                go = False
            
            elif data == 'no':    
    
                go = False
                addDeductions = False

            elif data == 'esc':

                print('Ending programm')

                os._exit(0)

            else:
    
                print('Ooops dont quite catch that, please re-inter these value')    
    else:

        print('''That's a total deduction of''', str(deduction))

        addDeductions = verifyBool('Would you like to add more enteries? If you do type yes, to exit type no ')



print('Ok thats an area of', area, 'square metres')

carpetType = input('What quality of carpet you want? Select 1 for low quality, 2 for medium quality and 3 for high quality ')

finalPrice = 0

if carpetType == '1':
    finalPrice = area * 3.50
elif carpetType == '2':
    finalPrice = area * 5.50
elif carpetType == '3':
    finalPrice = area * 7.50

#Discount

deduction = finalPrice / 10

print('''Its your lucky day. Since your new to JonJon's carept company, we are giving you a discount of 10 percent!''')

deductionStr = makePriceNum(deduction)

print('You save', deductionStr, ' pounds')

isDiscountCode = verifyBool('Do you have an additional discount code? ')


#Discount Codes and gift card data is stored on a seperate csv file, a database of sorts

if isDiscountCode == True:

    discountCodes = []
    
    code = input('Enter your discount code: ')

    with open('discountCodes.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

         discountCodes.append(discountVoucher(row['Code'], row['Deduction'], row['Type']))

        discountCodeFound = False
        deduction = 0
        deductionFinal = 0.0 

        for i in discountCodes:

            if i.Code == code:

                discountCodeFound = True

                if i.Type == 'Cash':

                    deduction = float(i.Deduction)

                    finalPrice -= deduction

                else:

                    cutter = finalPrice / 100

                    deduction = float(cutter) * float(i.Deduction)

                    deductionFinal = float(deduction)

                    finalPrice -= deductionFinal
        

        if discountCodeFound == True:

            deductionStr = makePriceNum(deductionFinal)

            print('Your discount code has been applied')
            print('You have saved', deductionStr)

adress = input('Where should we ship your carept to? ')
phoneNumber = input('What is your phone number so we can keep in contact? ')

finalPriceStr = makePriceNum(finalPrice)

print('Thanks for shopping with the JonJon carpeting company. Your final bill is' , finalPriceStr, 'pounds your carpet will be shipped to', adress)

