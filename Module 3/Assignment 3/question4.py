# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:33:23 2020

@author: sreet
"""

#Sreeti Ravi
#9-13-2020
#Question 4
#Write a program that asks the user for a positive integer n and then uses
#the counter pattern to find out and print the count of all numbers 1 and n,
#inclusive, which are divisible by 7.

def main():
    print("The program calculates the sum of numbers entered by the user.")
    
    n = int(input("How many numbers do you want to sum up? "))
    
    sum = 0
    for i in range(n):
        numbers = eval(input("Enter next number: "))
        sum = sum + numbers
    
    if n == 1:
        print("The sum of the", n, "number is", sum)
    else:
        print("The sum of the", n,"numbers is", sum)
    
main()