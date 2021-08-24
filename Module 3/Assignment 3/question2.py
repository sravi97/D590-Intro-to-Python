# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 01:23:29 2020

@author: sreet
"""

#Sreeti Ravi
#9-13-2020
#Question 2
#Write a program to determine the length of a ladder (in feet) required to 
#reach a given height when leaned against a house. Prompt the user for the 
#height (in feet) and angle (in degrees) of the ladder. Round the result to
#2 decimal digits.

import math

def main():
    print("The program calculates the length of a ladder.")
    height = int(input("Enter the height in feet: "))
    degrees = int(input("Enter the angle in degrees: "))
    
    radians = (math.pi/180) * degrees
    length = height/math.sin(radians)
    
    print("The length of the ladder is", round(length, 2), "feet.")
main()