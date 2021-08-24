# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:07:27 2020

@author: sreet
"""

#Sreeti Ravi
#10-03-20
#Assignment 6
#Question 2
#Write a function body_mass_index(height, weight) which receives height in 
#inches and weight in pounds, converts height to meters and weight to kilograms,
#then calculates and returns BMI.
#Function main() prompts for person’s height in inches and weight in pounds, 
#calls body_mass_index(height, weight) to determine BMI and prints the BMI and
#a message telling whether the person is above, within or below the healthy 
#range.
#Function main() uses exception to check if the user enters a non-number. The 
#function prints an error message and quits if the user enters a non-number or
#a negative number. 

def body_mass_index(height, weight):
    #Converts height to weight to proper units
    height = height * 0.0254
    weight = weight * 0.453592
    
    #Calculates BMI
    BMI = weight / (height ** 2)
    
    return BMI
    
def main():
    print("Program calculates the body mass index.")
    
    #Gets height from user and checks for valid input
    height = input("Enter your height in inches: ")
    try:
        height = float(height)
    except ValueError:
        print("Error! You entered a non-number.")
        return
    if height < 0:
        print("Error! You entered a negative number!")
        return
    
    #Gets weight from user and checks for valid input
    weight = input("Enter your weight in pounds: ")
    try:
        weight = int(weight)
    except ValueError:
        print("Error! You entered a non-number.")
        return
    if weight < 0:
        print("Error! You entered a negative number!")
        return
    
    BMI = body_mass_index(height, weight)
    #Checks what range BMI falls in and outputs corresponding message
    if BMI < 19:
        print("Your BMI is", BMI, ", you are under the healthy range!")
    elif 19 <= BMI <= 25:
        print("Your BMI is", BMI, ", you are in the healthy range!")
    elif BMI > 25:
        print("Your BMI is", BMI, ", you are above the healthy range!")

main()
    
    
    
    