# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 23:17:00 2020

@author: sreet
"""

#Exercise 3.1
#Write a program that takes two sides of a right-angled triangle and prints
#the longest side of a triangle
# import math

# def main():
#     a = int(input("Enter one side of a right triangle: "))
#     b = int(input("Enter second side of a right triangle: "))
    
#     c = math.sqrt(a**2 + b**2)
#     print("The longest side of the right triangle is", c)
    
# main()

#Exercise 3.2
#Write a program that prompts for the longest and ajacent side of a right 
#triangle, then calculates and prints the angle between them in both radians
#and degrees. 
#Print radians with 3 decimal digits, and degrees with 1 decimal digit

# import math

# def main():
#     adjacent = float(input("Enter the first side of a right triangle: "))
    
#     hyp = float(input("Enter the longest side of the triangle: "))
#     angle_r = math.acos(adjacent/hyp)
#     angle_d = (angle_r*180)/3.14
    
#     print("The angle in radians is", round(angle_r, 3))
#     print("The angle in degrees is", round(angle_d,1))

# main()

#Exercise 3.3
#Write a Python program to calculate the area A of a triangle (rounded to 1
#decimal digit) given the lengths of its three sides a,b and using the formulas:
#s=(a+b+c)/2
#A = sqrt(s(s-a)(s-b)(s-c))

# import math
# def main():
#     print("The program calculates the area of a triangle.")
#     a = eval(input("Enter the length of side a: "))
#     b = eval(input("Enter the length of side b: "))
#     c = eval(input("Enter the length of side c: "))
    
#     s = (a + b + c)/2
#     area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#     print("The area of the triangle is", round(area, 1))
    
# main()

#Exercise 3.4
#Use the accumulator pattern to find the sum of the first n natural numbers
#(positive integers), where the user provides the value of n.

# def main():
#     print("The program calculates the sum of first n natural numbers.")
    
#     n = int(input("Enter a positive integer: "))
#     total = 0
#     for i in range(n):
#         total = total + i
        
#     print("The sum of the first", n, "natural numbers is", total)
# main()

#Exercise 3.5
#Write a program that computes and prints the nth Fibonacci number, where
#n is a positive integer typed in by the user

# def main():
#     n = int(input("Enter a positive integer: "))
    
#     current, previous = 1, 1
    
#     for i in range(n-2):
#         current = current + previous
#         previous = current - previous

#     print(n,"th Fibonacci number is: ", current, sep = "")
# main()

#Exercise 3.6
#Write a program that approximates the value of pi by summing the terms of
#series(Leibniz formula):
# pi = 4/1 - 4/3 + 4/5 - 4/7 + 4/9 - 4/11
#the program should prompt the user for n, the number terms to sum, and then
#output the sum of the first n terms of this series.
#Have your program subtract the approximation from the value of math.pi
#to see how accurate it is

import math
def main():
    print("The program approximates the value of pi.")
    n = int(input("How many terms in series do you want to use?"))
    pi = 0
    
    for i in range(n):
        pi = pi 
    
    
    
    