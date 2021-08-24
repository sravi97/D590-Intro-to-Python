# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 01:01:55 2020

@author: sreet
"""

#Sreeti Ravi
#9/26/2020
#Question 4
#square_numbers(numbers), numbers is a list of numbers. Modifies the list numbers
#by squaring each entry
#sum_number(numbers), numbers is a list of numbers. Returns the sum of the 
#number in the list
#str_to_int(str_list), str_list is a list of strings, where each string 
#represents a number. Modifies each string in the list by converting it to a number
#main - use the previous three functions to compute the sum of the squares of 
#numbers in each line in a file

#Converts a list of strings to a list of numbers
def str_to_int(str_list):
    numbers = str_list.split()
    for number in range(0, len(numbers)): 
        numbers[number] = float(numbers[number])
    return numbers

#Squares the list of numbers from above
def square_numbers(numbers):
    numbers = [number ** 2 for number in numbers]
    return numbers

#Sums the list of squared numbers from above
def sum_numbers(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
 
def main():
    print("The program prints the sum of squares of each line in a file.")
    #Get filename from user
    file = input("Enter the name of file with numbers: ")
    
    #Open and read the lines of the file
    infile = open(file, 'r')
    linenum = 0
    str_list = infile.readlines()
    
    #Call methods from above and calculate line number
    for line in str_list:    
        numbers = str_to_int(line)
        
        square = square_numbers(numbers)

        linenum += 1
        sum = 0

        for number in square:
            sum += number
        
        print("Sum of squares in line", linenum, "is", sum_numbers(square))
            
       
    infile.close()
    
main()
