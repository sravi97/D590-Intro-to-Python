# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:34:27 2020

@author: sreet
"""

#Sreeti Ravi
#9-3-2020
#Question 3
# Modify the convert.py program so that it uses a "for" loop to compute and
# print at able of Celsius temperatures and the Fahrenheit equivalents every
# 10 degrees from 0C to 100C

def main():
    print("Conversion table from Celsius to Fahrenheit")
    print("  Celsius \t Fahrenheit\n------------------------")
    
    for celsius in range (0,110,10):
        fahrenheit= (9/5) * celsius+ 32
        print (" ", celsius, "\t\t\t",fahrenheit)
        
main()