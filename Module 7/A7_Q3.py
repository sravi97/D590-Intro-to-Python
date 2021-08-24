# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 01:12:55 2020

@author: sreet
"""

#Sreeti Ravi
#10/10/2020
#Question 3
#Program prints prime numbers in a range

def is_prime(number):
    #returns True if number is a prime number and otherwise False
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False
        
def display_primes(lower_bound, upper_bound):
    #prints all prime numbesr between lower_bound and upper_bound
    for i in range(lower_bound, (upper_bound + 1)):
        if(is_prime(i)):
            print(i)
    
def main():
    print("The program prints prime numbers in a range.")
    
    #prompts user for lower_bound integer
    lower_bound = input("Enter the lower limit of a range: ")
    
    #Exception handling to catch non-integer, print error message and quit
    try:
        lower_bound = int(lower_bound)
    except ValueError:
        print("Error! You entered a non-integer.")
        return
    if lower_bound < 1:
        print("Invalid input: Lower limit should be a positive integer, greater than 1.")
        return
    
    #prompts user for upper_bound integer
    upper_bound = input("Enter the upper limit of the range: ")
    
    #Exception handling to catch non-integer, print error message and quit
    try:
        upper_bound = int(upper_bound)
    except ValueError:
        print("Error! You entered a non-integer.")
        return
    
    #prints error message and quits in case lower_bound > upper_bound
    if upper_bound < lower_bound:
        print("Invalid input: Upper limit is less than lower limit.")
        return
        
    print("The sequence of prime numbers in the given interval: ")
    
    #calls display_primes(lower_bound, upper_bound) to print prime numbers in the interval
    display_primes(lower_bound,upper_bound)
    
   

main()