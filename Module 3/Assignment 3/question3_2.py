# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 01:39:19 2020

@author: sreet
"""

#Sreeti Ravi
#9-13-2020
#Question 3.2
#Write a program that asks the user for a positive integer n and then uses
#the counter pattern to find out and print the count of all numbers 1 and n,
#inclusive, which are divisible by 7.

def main():
    print("The program prints the count of numbers divisible by 7.")
    
    n = int(input("Enter a positive integer: "))
    counter = 0
    
    for i in range(1,n+1):
        if (i % 7) == 0:
            counter = counter + 1
        
    if counter == 1:
        print("There is", counter, "number between 1 and", n, "that is divisible by 7.")
    else:
        print("There are", counter, "numbers between 1 and", n, "that are divisible by 7.")

main()