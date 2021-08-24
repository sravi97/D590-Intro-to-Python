# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 00:34:26 2020

@author: sreet
"""

#Sreeti Ravi
#9-3-2020
#Question 2
#Write a program that prompts the user for the mileage of a vehicle, calculates
#and prints the fuel consumption of the vehicle in liters per 100 km. Assume
#that 1 mile is 1.6 km and 1 gallon is 3.785 liters.

def main():
    print("The program converts mileage to liters per 100 km.")
    
    miles = eval(input("Please enter mileage (miles per gallon): "))
    liters = (3.785 * 100)/(miles * 1.6)
    
    print("\nVehicle economy is", miles, "miles per gallon.")
    print("Vehicle consumption is", liters, "liters per 100 km.")
main()
