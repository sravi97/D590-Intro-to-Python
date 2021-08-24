# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:31:40 2020

@author: sreet
"""

#Sreeti Ravi
#9/19/2020
#Question 4
#A palindrome is a word, phrase, or sequence that reads the same backwards as 
#forwards. Write a program that prompts the user for a string, determines if
#the string is a palindrome and prints "The string is palindorme" or "The string
#is not a palindrome."

def main():
    print("The program checks if an input string is a palindrome.")
    
    string = input("Enter a string: ")
    reverse = ''
    
    for letter in string:
        reverse = letter + reverse
        
    if string == reverse:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
    

main()