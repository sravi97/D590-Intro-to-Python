# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:34:53 2020

@author: sreet
"""

#Sreeti Ravi
#10-25-20
#Assignment 9
#Question 4
#Write a Python program that uses NumPy to calculate and print average of each
# assignment group. 

import numpy as np

def main(): 
    print("Program to calculate assignment group averages. \n")
    
    #read file scores.npy
    scores = np.load("scores.npy")
    scores_only = scores[1:, :]
    
    #calculating homework average
    hw_scores = (scores_only[:, 1:7].sum(axis=0))

    hw_total = 0
    for i in hw_scores:
        hw_total += i
    
    print("Homework average:  ", np.around(hw_total/264), "\n")
    
    #calculating lab average
    lab_scores = (scores_only[:, 7:18].sum(axis=0))

    lab_total = 0
    for i in lab_scores:
        lab_total += i
    
    print("Lab average:       ", np.around(lab_total/484), "\n")
    
    #calculating quiz average
    quiz_scores = (scores_only[:, 20:29].sum(axis=0))

    quiz_total = 0
    for i in quiz_scores:
        quiz_total += i
    
    print("Quiz average:       ", np.around(quiz_total/396), "\n")
    
    #calculating project average   
    final_project_avg = (scores_only[:, 18:19].sum(axis=0)/44)

    for i in final_project_avg:   
        print("Project average:   ", np.around(i, decimals = 1), "\n")
        
    #calculating midterm 1 average
    midterm1_avg = (scores_only[:, 19:20].sum(axis=0)/44)

    for i in midterm1_avg:   
        print("Midterm 1 average: ", np.around(i, decimals = 1), "\n")
    
    #calculating midterm 2 average
    midterm2_avg = (scores_only[:, 29:30].sum(axis=0)/44)

    for i in midterm2_avg:   
        print("Midterm 2 average: ", np.around(i, decimals = 1), "\n")

main()