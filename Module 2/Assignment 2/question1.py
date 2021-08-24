# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:34:25 2020

@author: sreet
"""

#Sreeti Ravi
#9-3-2020
#Question 1
#Write a program that prompts the user for the distance in kilometers, converts
#and prints the distance in miles. One km is ~0.62 miles.

def main():
    print("The program converts kilometers to miles.")
    
    km = eval(input("Enter the distance in kilometers: "))
    mi = km * 0.62
    print("The distance is", mi, "miles.")
main()