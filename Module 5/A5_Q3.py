# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 23:25:46 2020

@author: sreet
"""

#Sreeti Ravi
#9/26/2020
#Question 3
#Write a function called factorial(choices) that takes an integer input
#choices and returns the factorial. 
#Then, write a program which asks for two non-negative integer inputs; 
#one for choices and another for slots. If either of the inputs are negative,
#it returns an error message that the input needs to be non-negative. If the
#input for choices is less than the input for slots, then it returns an error
#message that choices cannot be less than slots.

#Takes an integer input choices and returns the factorial
def factorial(choices):
    factorial = 1
    for i in range(1, choices + 1):
        factorial = factorial * i
    return factorial


def main():
    #Get inputs from the user
    choices = eval(input("Enter a non-negative integer for the number of choices: "))
    slots = eval(input("Enter a non-negative integer for the number of slots: "))
    
    #Calculate the denominator
    denominator = 1
    for i in range (1, (choices-slots+1)):
        denominator = denominator * i

    permutation = factorial(choices) / denominator
    
    if choices > slots and choices > 0 and slots > 0:
        print("Number of permutations P( ", choices, ",", slots, ") = ", permutation)
    elif choices < slots:
        print("Error! Number of choices is less than the number of slots.")
    elif choices < 0 or slots < 0:
        print("Error! The number of choices or slots cannot be negative.")
    elif type(choices) == string or type(slots) == string:
        print("Not a number")        
main()