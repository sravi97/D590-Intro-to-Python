# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:17:23 2020

@author: sreet
"""


#Sreeti Ravi
#9/26/2020
#Question 5
#Write function count_digits(line), which counts and returns the number of digits
#in a string line
#Write a main() that prompts the user for the name of a text file, and uses the
#previous function to count and print the total number of digits in each line
#of the text file

#Returns the number of digits in a line
def count_digits(line):
    count = 0
    for c in line:
        if c.isdigit() == True:
            count += 1
    return count
            

def main():
    print("The program prints the number of digits in each line of a file.")
    
    #Get file from user and open the file.
    file = input("Enter the name of input text file: ")
    infile = open(file, 'r')
    
    #Calculate line number
    line_num = 0
    for line in infile:
        line_num += 1

        print("There are", count_digits(line), "digits in line", line_num)
        
main()