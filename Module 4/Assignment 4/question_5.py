# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:31:41 2020

@author: sreet
"""

#Sreeti Ravi
#9/19/2020
#Question 5
#Write a program that reads a file, counts and prints the number of words in
#the file

def main():
    print("The program counts numbers of words in an input file.")
    
    fname = input("Enter a file name: ")
    infile = open(fname, 'r')
    
    count = 0
    for line in infile.readlines():
       count += len(line.split())
    
    print("There are", count, "words in the file.")
    
main()
    