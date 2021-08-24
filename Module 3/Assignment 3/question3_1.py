# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 01:32:45 2020

@author: sreet
"""

#Sreeti Ravi
#9-13-2020
#Question 3.1
#Write a program that asks the user for a positive integer n and then prints
#all numbers between 1 and n, inclusive, which are divisible by 3.

def main():
    print("The program prints the numbers divisible by 3.")
    
    n = int(input("Enter a positive integer: "))
    print("Numbers between 1 and", n, "divisible by 3 are:")
    for i in range(n+1):
        if i % 3 == 0 :
            print ("\t",i)

main()