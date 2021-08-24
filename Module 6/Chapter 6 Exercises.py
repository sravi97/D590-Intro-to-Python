# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 00:19:09 2020

@author: sreet
"""

#Exercise 6.1
#A college classifies students according to credits earned. A student with less
#than 30 credits is a freshman. At least 30 credits are required to be a 
#sophomore, 60 to be a junior, and 90 to be a senior.
#Write a function class_standing(credits) that calculates standing from the 
#number of credits earned 
#Function main() asks the user for the number of credits, calls class_standing(credits)
#to determine and print the college classification
#Function main() prints error message if the user enters a non-number or a number
#which is outside range from 0 to 100

# def class_standing(credits):
#     if credits < 30:
#         return "freshman"
#     elif credits < 60:
#         return "sophomore"
#     elif credits < 90:
#         return "junior"
#     else:
#         return "senior"

# def main():
#     print("College classification")
#     credits = input("Please enter number of credits: ")
    
#     try:
#         credits = float(credits)
#     except ValueError:
#         print("Input Error! You entered a non-number!")
#         return
    
#     if (credits < 0) or (credits > 100):
#         print("Input error! Number of credits should be between 0 and 100!")
#         return
    
#     print("You are", class_standing(credits))

# main()

#Exercise 6.2
#The speeding ticket fine policy in Bloomville is $50 plus $5 for each mph over
#the limit plus a penalty of $200 for any speed over 90 mph. Write a program
#that accepts a speed limit and a clocked speed and either prints a message
#indicating the speed was legal or prints the amount of the fine (rounded to
#an integer), if the speed is illegal
#Print error message in case of illegal user input

# def main():
#     print("Speeding fine calculator.")
#     speed_limit = input("Enter the speed limit: ")
#     try:
#         speed_limit = float(speed_limit)
#     except:
#         print("Input error! You entered a non-number!")
#     if speed_limit < 0:
#         print("Input error! Speed limit should be a positive number!")
            
#     clocked_speed = input("Enter the clocked speed: ")
#     try:
#         clocked_speed = float(clocked_speed)
#     except:
#         print("Input error! You entered a non-number!")
#     if speed_limit < 0:
#         print("Input error! Speed limit should be a positive number!")
        
#     fine = ((clocked_speed - speed_limit) * 5) + 50
#     if clocked_speed > 90:
#         fine += 200
    
#     print("Your speeding fine is", int(fine), "dollars.")
    
# main()

#Exercise 6.3
#Write functions digits_and_letters that accepts a string and uses counter pattern
#to calculate and return the number of digits and letters in the sentence
#Write a main() function that prompt the user for a sentence, calls function
#digits_and_letters(sentence) to determine and print he number of digits and
#letter in the sentence

# def digits_and_letters(string):
#     digits = letters = 0
    
#     for char in string:
#         if char.isdigit():
#             digits += 1
#         if  char.isalpha():
#             letters += 1
#         else:
#             pass
    
#     return digits, letters
    
# def main():
#     print("The program counts the number of digits and letters.")
#     sentence = input("Please type in a sentence: ")
    
#     digits, letters = digits_and_letters(sentence)
    
#     print("There are ", digits, "in the sentence.")
#     print("There are ", letters, "in the sentence.")
    
# main()

#Exercise 6.4
#Assume that a valid file name: has first character that is a letter, contains
#at least one digit, contains no period(.) or comma(,)
#Write function check_file_names, which returns True if the string s conforms
#to the above criteria and False otherwise
#write a main() function that prompts the user for a string, calls function
#check_file_name(name) to determine if the input string is a valid name
#and accordingly prints a message

def check_file_name(name):
    if s[0] .isdigit():
        
    
def main():
    print("The program checks if the input string is a valid file name.")
    s = input("Please enter a string: ")
    
    
    
        
    