# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:01:49 2020

@author: sreet
"""

#Sreeti Ravi
#9/26/2020
#Question 2
#Write two functions:
#encrypt(plaintext, shift): which encrypts a string of lower case letters 
#using the Caesar cipher and then prints the encrypted text
#decrypt(ciphertext, shift): which takes a string that has been encrypted 
#using the Caesar cipher, and decrypts it so it's original form
#Write a main() that prompts the user for a mode to encrypt or decrypt, a 
#string for encryption/decryption, and the shift that should be used

letters = 'abcdefghijklmnopqrstuvwxyz'

#Encrypts a string of lower case letters using the Caesar cipher and prints
#the encrypts text
def encrypt(plaintext, shift):
    encrypted_str = ""
    for letter in plaintext:
        index = letters.find(letter) + shift
        if index > 26:
            index = index - 26
        else:
            index
        encrypted_str += letters[index]
    return encrypted_str    
        
#Takes a string that has been encrypted and decrpyts it to it's original form
def decrypt(ciphertext, shift):
    encrypted_str = ""
    for letter in ciphertext:
        index = letters.find(letter) - shift
        if index > 26:
            index = index - 26
        else:
            index
        encrypted_str += letters[index]
    return encrypted_str    

def main():
    #Choose a mode
    mode = input("Choose a mode: [e]ncryption or [d]cryption? ")
    
    #If user chooses encryption
    if mode == 'e':
        plaintext = input("Enter the text: ")
        shift = eval(input("Enter the shift for the cipher (-25 to 25): "))
        print("Result: ", encrypt(plaintext, shift))
    #If user chooses decryption    
    if mode =='d':
        ciphertext = input("Enter the text: ")
        shift = eval(input("Enter the shift for the cipher (-25 to 25): "))
        print("Result: ", decrypt(ciphertext, shift))
main()