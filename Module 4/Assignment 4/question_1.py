# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:31:21 2020

@author: sreet
"""

#Sreeti Ravi
#9/19/2020
#Question 1
#Write a program that takes an input string from the user and prints the string
#in a reverse order

def main():
    print("The program prints a string in a reverse order")
    
    s = input("Please enter a string: ")
    print()
    
    print("You typed a string: ", s)
    print("The string in the reverse order: ", end="")
    
    for i in range(1, len(s) + 1):
        print(s[len(s)-i], end="")
        
main()