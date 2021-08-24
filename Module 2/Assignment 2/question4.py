# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:34:34 2020

@author: sreet
"""

#Sreeti Ravi
#9-3-2020
#Question 4
#Write an interactive Python calculator program. The program should allow the
#user to type a mathematical expression, and then print the value of the
#expression. Include a for loop so that the user can perform many calculations

def main():
    print("Welcome to the Interactive Python Calculator")
    for i in range(100):
        expression = eval(input("Enter an expression: "))
        print(expression)

main()
