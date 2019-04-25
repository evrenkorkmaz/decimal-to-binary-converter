"""
@author : Evren Korkmaz

Date : 25/04/2019
"""

number=int(input("Enter an integer:")) #
binary=""  # define a binary string for save binary value
while number>=2: # loop for division and mod operation
    binary=str(number%2)+binary # mod operation
    number=number//2 #division operation

binary=str(number)+binary # the last value is added 
print(binary) #prints a binary value on the screen
