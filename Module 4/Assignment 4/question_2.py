# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:31:40 2020

@author: sreet
"""

#Sreeti Ravi
#9/19/2020
#Question 2
#Write a program that takes a positive integer number from the user and prints
#the number in words

def main():
    print("The program spells the input number.")
    
    number = input("Please input a number: ")
    
    numbers = ["one","two","three","four","five","six","seven","eight",
               "nine", "zero"]
    
    words = ""
    for i in number:
        words += (numbers[int(i) - 1] + " ")
    print("The number in words: ", words)
        
main()
    