# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:34:52 2020

@author: sreet
"""

#Sreeti Ravi
#10-25-20
#Assignment 9
#Question 1
#Write a Python program that uses NumPy to:
    #Read "scores_all.csv"
    #Remove the first row (with column headings)
    #Fill out the missing data with 0s
    #Print the resulting data array and save it to the file  "scores.npy"
    
import numpy as np

def main():
    #read data from file
    s = np.genfromtxt("scores_all.csv", delimiter = ",", skip_header=1)
    
    #identify elements with NaN
    blanks = np.isnan(s)
    
    #replace NaN with 0s
    scores = np.where(blanks, 0, s)
    
    #convert numpy array to integers
    scores = scores.astype(int)
    
    #save array to file
    np.save("scores", scores )
    
    #print data array
    print(np.load("scores.npy"))

main()
    