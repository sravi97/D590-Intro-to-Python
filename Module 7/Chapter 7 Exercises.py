# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Exercise 7.1
#Write a program to print the multiplication tables for numbers 1 to 9, inclusive.
# def main():
#     print("A program to print multiplication tables for numbers 1 to 10.")
    
#     for i in range(1,10):
#         print("Multiplication table for number", i)
#         for j in range(1, 11):
#             print(i, 'x', j, "=", i*j)
        
# main()

#Exercise 7.2
#Write a program that approximates the value of pi by summing the terms given
#by Leibniz formula.

# def main():
#     print("The program calculates pi to a required precision.")
#     import math
    
#     delta = input("What precision do you want to calculate pi? ")
#     try:
#         delta = float(delta)
#     except ValueError:
#         print("Input error! You entered a non-number!")
#         return
    
#     delta = abs(delta)
    
#     pi = 0
#     sign = 1.0
    
#     i = 0
#     prev = 4
#     while (abs(pi - prev) > delta):
#         prev = pi
#         pi = pi + sign * 4 / (2*i + 1)
#         i = i + 1
#         sign = - sign
    
#     print("\nThe calculation was done in", i, "iterations")
#     print("The difference between last two approximations of pi:", abs(pi - prev))
#     print("The approximation of number pi is", pi)
#     print("Difference from math.pi:", abs(round((math.pi - pi), 10)))

# main()        
        
#Exercise 7.3
#Write a program that prompts the user to enter a sequence of integers, each
#number in a separate line, with no duplicates. User ends the input by
#pressing enter with no input number.
#Print error message in case the user enters a duplicate. Ignore duplicate and
#continue execution
#Use exception to detect if the user enters a non-integer, print error
#message and continue execution
#Print the resulting sequence of numbers (with no duplicates)

def main():
    print("Program to enter a sequence of integers with no duplicates.")
    number = input("Please enter an integer (Enter to end): ")
    
    try:
        number = int(number)
    except ValueError:
        print("Error! Please enter a valid integer: ")
        
        
    
    
    
    
    