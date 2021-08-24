# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 19:34:53 2020

@author: sreet
"""

#Sreeti Ravi
#10-25-20
#Assignment 9
#Question 3
#Write a Python program that uses NumPy to calculate and print average score 
#for each assignment.
import numpy as np

def main():
    #read scores.npy
    scores = np.load("scores.npy")
    
    #get rid of weights
    scores_only = scores[1:, :]
    
    #calculating average for homeworks
    hw_number = 0

    for hw_number in range(6):
        score = (scores_only[:, hw_number+1].sum(axis=0)/44)
        
        print("Homework", hw_number, "average: \t", np.around(score, decimals = 1))
    
        hw_number += 1

    print("\n")
    
    #calculating average for labs
    lab_number = 0

    for lab_number in range(11):
        score = (scores_only[:, lab_number+7].sum(axis=0)/44)

        lab_number += 1
    
        print("Lab \t", lab_number, "average: \t", np.around(score, decimals = 1))
      
    print("\n")
    
    #calculating average for quizzes
    quiz1_average = (scores_only[:, 20].sum(axis=0)/44)
    quiz2_average = (scores_only[:, 21].sum(axis=0)/44)
    quiz3_average = (scores_only[:, 22].sum(axis=0)/44)
    quiz5_average = (scores_only[:, 23].sum(axis=0)/44)
    quiz6_average = (scores_only[:, 24].sum(axis=0)/44)
    quiz7_average = (scores_only[:, 25].sum(axis=0)/44)
    quiz8_average = (scores_only[:, 26].sum(axis=0)/44)
    quiz9_average = (scores_only[:, 27].sum(axis=0)/44)
    quiz10_average = (scores_only[:, 28].sum(axis=0)/44)
    
    quiz_avg = [quiz1_average, quiz2_average, quiz3_average, quiz5_average, quiz6_average,
                quiz7_average, quiz8_average, quiz9_average, quiz10_average]

    quiz_counter = 1
    for i in quiz_avg:
        if quiz_counter == 4:
            quiz_counter += 1
        print("Quiz \t", quiz_counter, "average: \t", np.around(i, decimals=1))
        quiz_counter += 1
    
    print("\n")
    
    #calculating average for final project
    final_project_avg = (scores_only[:, 18:19].sum(axis=0)/44)

    for i in final_project_avg:   
        print("Final project avg: ", np.around(i, decimals = 1))
        
    
    #calculating average for midterm 1
    midterm1_avg = (scores_only[:, 19:20].sum(axis=0)/44)

    for i in midterm1_avg:   
        print("Midterm 1 average: ", np.around(i, decimals = 1))
    
    
    #calculating average for midterm 2
    midterm2_avg = (scores_only[:, 29:30].sum(axis=0)/44)

    for i in midterm2_avg:   
        print("Midterm 2 average: ", np.around(i, decimals = 1))

    
main()