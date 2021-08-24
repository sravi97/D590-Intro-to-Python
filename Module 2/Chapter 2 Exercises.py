# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 23:01:01 2020

@author: sreet
"""

#Chapter 2

#Exercise 2.1
#Write a program, which accepts the user's first and last name, prints them 
#in reverse order and terminates

# def main():
#     print("The program prints the first and last name in reverse order.")
#     firstName = input("Enter your first name: ")
#     lastName = input("Enter your last name: ")
#     print("Hello", lastName, firstName)

# main()

#Exercise 2.2
#Write a program, which prompts the user for a radius of a sphere, calculates
#and prints the volume of a sphere

# def main():
#     radius = eval(input("Enter radius of a sphere: "))
#     volume = (4/3) * 3.1416 * radius ** 3
#     print("The volume of the sphere is", volume)
    
# main()

#Exercise 2.3
#Write a program that asks the user to enter their name and their age (as
#integer). Print out a message addressed to them that tells them the year
#they will turn 100 years old

# def main():
#     name = input("What is your name: ")
#     age = int(input("How old are you: "))
#     year = 100 - age + 2020
#     print(name,"will be 100 years old in the year", year)

# main()

#Exercise 2.4
#Write a Python program that prompts the user for the values of x and y, 
#solves (x+y) * (x-y), and prints the result.

# def main():
#     print("The program solves (x + y) * (x - y).")
    
#     x, y = eval(input("Enter the values of x and y separated by comma:"))
#     output = (x + y) * (x - y)
#     print("(x + y) * (x - y) =", output)
    
# main()

#Exercise 2.5
#Write a Python program that prints the first 10 integers (starting from 1)
#and then prints the same integers in reverse order. Print each integer in a
#separtae line.

# def main():
#     print("The first ten integers: ")
#     for i in range(10):
#         print(i+1)
    
#     print("The first ten integeres in reverse order: ")
#     for i in range(10,1,-1):
#         print(i)
# main()

#Example 2.7
#Write a Python program that prompts the user for an integer n, and then
#prints n lines with 10 stars in each line.
# def main():
#     x = eval(input("Enter an integer: "))
#     star = ("**********\n")
#     print(star * x)
    
# main()  

#Example 2.8
#Write a program that prompts the user for a positive integer n, then 
#calculates and prints the sums of first i integers, for i=0,1,2,...,n-1

def main():
    x = eval(input("Enter an integer: "))
    for i in range (x):
        total = i*(i+1)/2
        print("The sum of first", i, "integers is",total)

main()


