# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 01:13:28 2020

@author: sreet
"""

#Sreeti Ravi
#9-13-2020
#Question 1
#Write a Python program, which prompts the user for the temperature and wind 
#speed, then calculates and prints the wind chill rounded to one digit after
#the decimal point
import math

def main():
    print("The program calculates the wind chill.")
    temp = int(input("Enter the temperature in degrees Fahrenheit: "))
    wind_speed = int(input("Enter wind speed in miles per hour: "))
    
    wind_chill= 35.74 + 0.6215*temp - 35.75*math.pow(wind_speed,0.16) + 0.4275*temp*math.pow(wind_speed,0.16)
    
    print("The wind chill index is", round(wind_chill,1))
main()