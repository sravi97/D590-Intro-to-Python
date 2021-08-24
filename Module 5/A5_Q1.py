# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 20:15:13 2020

@author: sreet
"""
#Sreeti Ravi
#9/26/2020
#Question 1
#Write definitions for two functions:
#sum_numbers(numbers) returns the sum of the first n positive integers
#sum_cubes(numbers) returns the sum of the cubes of the first n positive integers
#Write main() that prompts the user for a positive integer n, calls the above
#functions and prints out the sum of the first n integers and the sum of the 
#cubes of the first n integers

#returns the sum of the first n numbers
def sum_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

#returns the sum of the cubes of the first n numbers             
def sum_cubes(numbers):
    cube_sum = 0
    for number in numbers:
        cube_sum += number**3
    return cube_sum
    
def main():
    print("The program calculates the sum of first n numbers and sum of their cubes.")
    n = eval(input("Please enter a positive integer: "))
       
    numbers = range(n + 1)
       
    if n <= 0:
          return 

    print("The sum of first", n, "positive integers is", sum_numbers(numbers))
    print("The sum of first", n, "positive integers is", sum_cubes(numbers))
main()