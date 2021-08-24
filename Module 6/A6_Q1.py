# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:07:27 2020

@author: sreet
"""

#Sreeti Ravi
#10-03-20
#Assignment 6
#Question 1
#Write a function letter_grade(score) which receives a score and uses 
#decision structure to calculate and return the corresponding letter grade 
#without the plus and minuses.
#Write a function plus_or_minus(score) which receives a score and uses decision
#structure to calculate and return the corresponding “+” or “-“ or “”.
#Function main() prompts the user for the score, calls letter_grade to convert
#the score into a letter grade, and calls plus_or_minus to determine if there 
#is a plus or a minus, and prints the letter grade with the plus or minus if 
#necessary.
#Use exception to check if the user enters a non-integer. If the user enters a 
#non-integer or a number outside range 0 to 100, main() prints appropriate 
#message and terminates. 

#calculates and returns the corresponding letter grade without + or -
def letter_grade(score):
    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"

#Receives a score and returns +, - or nothing
def plus_or_minus(score):
    if score == 100:
        return "+"
    elif 0 <= (score % 10) < 3:
        return "-"
    elif 6 <= (score % 10) <= 9:
        return "+"
    else:
        return ""
    
def main():
    print("Program calculates the letter grade from a total score.")
    #Gets input from user
    score = input("Enter your total score: ")
    
    #Checks if input is valid
    try:
        score = int(score)
    except ValueError:
        print("Error! You entered a string that is not a number!")
        return
    
    #Checks if input is in range
    if (score < 0) or (score > 100):
        print("Error! The total score must be between 0 and 100.")
        return
    
    #Combines letter grade and plus or minus
    grade = letter_grade(score) + plus_or_minus(score)
    
    print("Your letter grade is", grade)
    
main()