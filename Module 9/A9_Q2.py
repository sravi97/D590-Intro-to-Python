# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:34:53 2020

@author: sreet
"""

#Sreeti Ravi
#10-25-20
#Assignment 9
#Question 2
#Write a Python program that uses NumPy to read file "scores.npy" and create a
#NumPy array "score_headings" with the following columns:
#ID numbers, weighted scores for the hw assignment, weighted scores for the labs,
#weighted final project scores, weighted midterm 1 scores, weighted scores for 
#the quizzes, weighted midterm 2 scores
#Print score_headings and store it to the file score_heading.npy

import numpy as np

def main():
    #read file score.npy
    scores = np.load("scores.npy")
    
    #selecting only needed columns and dropping headings
    scores_only = scores[1:, :]
    
    #fancy indexing to extract ifnormation
    scores2 = scores_only[:, [0, 1, 2, 3, 4, 5, 6]]
    m, n = scores2.shape
    
    score_headings = np.zeros([m, n])
    
    #id numbers
    score_headings[:, 0] = scores2[:, 0]
    
    #calculating weighted scores
    score_headings[:, 1] = (((scores_only[:, 1:7]).sum(axis = 1))/600) * 20
    score_headings[:, 2] = (((scores_only[:, 7:18]).sum(axis = 1))/1100) * 30
    score_headings[:, 3] = (((scores_only[:, 18:19]).sum(axis = 1))/100) * 10
    score_headings[:, 4] = (((scores_only[:, 19:20]).sum(axis = 1))/100) * 10
    score_headings[:, 5] = (((scores_only[:, 20:29]).sum(axis = 1))/90) * 15
    score_headings[:, 6] = (((scores_only[:, 29:30]).sum(axis = 1))/100) * 15
    
    #save score_headings to a file
    np.save("score_headings", score_headings)
    
    #print with elements rounded
    print(np.around(score_headings, decimals = 1))
        
main()