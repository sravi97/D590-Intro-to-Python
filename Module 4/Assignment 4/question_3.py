# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:31:40 2020

@author: sreet
"""

#Sreeti Ravi
#9/19/2020
#Question 3
#Suppose that the value of a name is determined by summing up the values of the 
#letters of the name where 'a' is 1, 'b' is 2, 'c' is 3 etc., up to 'z' being 26.
#For example, the name "dog" would have the value 4+15+7 = 26. Write a program
#that calculates the numeric value of a single name (in lower case letters) as input.

def main():
    print("The program computes the value of a string.")
    
    name = input("Enter any name in lower case: ")
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    value = 0
    for letter in name:
       value += (letters.find(letter) + 1)
    
    print("The numeric value of the name is", value)
main()