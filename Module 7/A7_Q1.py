# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 01:12:54 2020

@author: sreet
"""

#Sreeti Ravi
#10/10/2020
#Question 1
#Program prints min, max, and count of positive and negative numbers

#Takes as input a list of integers and returns the values of the 
#smallest and largest integer.
def get_min_max(integers):
    smallest = min(integers)
    largest = max(integers)
    
    return smallest, largest   
    
#takes as input a list of integers
def count_signed_integers(integers, whole=False):
    #initialize variables to keep track of counts
    positive = 0
    negative = 0
    zeros = 0
    
    #parsing through the integers to identify positives, negatives and zeros
    for s in integers:
        if s == 0:
            whole = True
            if whole == True:
                zeros += 1 
        if s > 0:
            positive += 1
        if s < 0:
            negative += 1
    
    #returns counts of positives, negatives, zeros and Boolean value for whole
    return positive, negative, zeros, whole
    
def main():
    print("Program prints min, max, and count of positive and negative numbers")
    
    integers = []
    s = input("Enter a number: ")
    
    #sentinel loop to continually prompt user to enter integers until empty string
    while s != "":
        
        #exception handling to catch if user enters a non-number
        try:
            x = int(s)
            s = input("Enter a number: ")
            integers.append(x)
        
        #print error message if non-number and continue execution
        except ValueError:
            s = input("Error! Please enter a valid number: ")
    
    #calls get_min_max() to smallest and largest integers
    smallest, largest = get_min_max(integers)
    positive, negative, zeros, whole = count_signed_integers(integers, whole=False)
    
    print("You entered", len(integers), "numbers.")
    print("The smallest number is", smallest)
    print("The largest number is", largest)
    
    
    if whole == False:
        print("There are", positive, "positive and", negative, "negative number(s)")
    else:
        print("There are", positive, "positive and", negative, "negative number(s), and", zeros, "zeros.")
    
    
main()