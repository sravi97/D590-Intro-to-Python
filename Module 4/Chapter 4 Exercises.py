# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:52:10 2020

@author: sreet
"""

#Exercise 4.1
#Write a program that inputs an integer n from the user and prints n lines, 
#such that there are i stars in line i = 1, 2, ... n . 

# def main():
#     print("The program prints a triangle of stars with n lines.")
    
#     n = int(input("Enter an integer n: "))
    
#     for i in range(n+1):
#         print(i * "*")

# main()

#Exercise 4.2
#Write a program that takes integers from the user and prints the horizontal
#histogram (with the stars) of the input numbers

# def main():
#     print("The program prints a histogram of input numbers.")
    
#     in_line = input("Please input numbers and hit Enter: ")
#     in_list = in_line.split()
    
#     print()
#     for i in in_list:
#         print(int(i) * "*")
# main()

#Exercise 4.3
#The letter grade in a course is determined on the scale 90-100 points: A,
#80-89: B, 70-79: C, 60-69: D, <60: F. Write  a program with no conditional
#statements, that accepts a score in points and prints out the corresponding
#letter grade

# def main():
#     print("The program prints a letter grade.")
#     score = int(input("Please input a score between 0 and 100: "))
    
#     letter_grade = 60*"F" + 10*"D" + 10*"C" + 10*"B" + 10*"A"
#     print("The letter grade is", letter_grade[score])
# main()

#Exercise 4.4
#Write a program that allows the user to type in a phrase and then outputs
#the acronym for that phase. The acronym should be all uppercase, even if the
#words in the phrase are not capitalized

# def main():
#     print("The program prints an acronym for an input phase.")
#     phrase = input("Please input a phrase: ")
#     words = phrase.split()
    
#     acronym = ""
#     for letter in words:
#         acronym = acronym + letter[0]

#     print("The acronym is", acronym.upper())
        
# main()

#Exercise 4.5
#Write a program that calcualtes the average word length in a sentence entered
#by the user.

# def main():
#     print("The program calculates the average word length.")
    
#     sentence = input("Please input as sentence: ")
#     words = sentence.split()
    
#     c = 0
#     for letter in words:
#         c = c + len(letter)
        
#     average = c/len(words)
#     print("The average word length is", average)
        
# main()

#Exercise 4.6 
#Write a program that prints the largest number from the numbers entered by
#the user

# def main():
#     print("The program finds the largest number.")
    
#     numbers = input("Please enter the numbers: ")
#     number_list = numbers.split()
    
#     largest = eval(number_list[0])
    
#     for number in number_list:
#         if eval(number) > largest:
#             largest = eval(number)
    
#     print("The largest number is", largest)
    
# main()

#Exercise 4.7
#Write a Python program that prompts the user to enter a sequence of strings. 
#Use counter pattern to find the number of strings where first and last character
#are same from a given sequence of strings

# def main():
#     print("The program counts the strings with the same first and last character.")
    
#     strings = input("Please enter a sequence of strings: ")
#     string_list = strings.split()
    
#     count = 0
#     for string in string_list:
#         if string[0] == string[-1]:
#             count = count + 1
    
#     print ("There are", count, "strings where the first and last characters are same.")
# main()

#EXercise 4.8 
#Write a Python program that prompts the user to enter a sequence of strings
#and then prints all strings that are longer than 5 characters

# def main():
#     print("The program prints the strings that are longer than 5 characters.")
    
#     strings = input("Please enter a sequence of strings: ")
#     strings_list = strings.split()
#     print()
#     print("The strings that are longer than 5 characters: ")
#     for string in strings_list:
#         if len(string) > 5:
#             print(string)

# main()
