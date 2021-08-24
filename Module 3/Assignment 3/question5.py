# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 11:39:26 2020

@author: sreet
"""

#Sreeti Ravi
#9-13-2020
#Question 5
#Write a program, which prompts the user for two positive integers, start and
#end that defien a range of numbers, including both start and end. The program
#calculates and prints the ratio of the sum of even numbers to the sum of all
#the numbers in the range (rounded to three decimal digits).

def main():
    start = int(input("Enter start number of a range: "))
    end = int(input("Enter ending number of a range: "))
    
    even_sum = 0
    total_sum = 0
    
    for i in range(start, end+1):
        if (i % 2)==0:
            even_sum = even_sum + i
            total_sum = total_sum + i
        else:
            total_sum = total_sum + i
    ratio = even_sum/total_sum
    print("Ratio of sum of even numbers to sum of all numbers in the range is", round(ratio,3))

main()