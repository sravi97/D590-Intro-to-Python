# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:07:27 2020

@author: sreet
"""

#Sreeti Ravi
#10-03-20
#Assignment 6
#Question 4
#A website requires the users to input username and password to register. Write
#a program to check the validity of password input by users. Following are the
#criteria for checking the password:
#• Minimum length of password: 4 characters
#• Maximum length of password: 8 characters
#• First character has to be a letter
#• At least 1 number between [0-9]
#• At least 1 character from [$#@]
#In case a user enters an invalid password, the program prints an error message
#indicating the type of error, and quits. 

def main():
    print("The program checks passwords.")
    #Gets input from user
    password = input("Please enter a password: ")
    
    #Initialize variables to keep track of whether requirements have been met
    special_char = False
    number = False
    
    #Checks if password is the correct length
    if len(password) < 4:
        print("Error: The password has less than 4 characters!")
        return
    elif len(password) > 8:
        print("Error: The password has more than 8 characters!")
        return
    
    #Checks if the first character is a letter
    if password[0].isdigit():
        print("The first character has to be a letter.")
    
    #Checks if there is one special charcter and number
    for char in password:
        if char.isdigit():
            number = True
        if char in '$#@':
            special_char = True
    
    if number == False:
        print("Error: The password does not have at least one number.")
    if special_char == False:
        print("Error: The password does not have at least character from [$#@]!")
    else:
        print("You entered a valid password.")

    
main()