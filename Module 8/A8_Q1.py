# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:11:09 2020

@author: sreet
"""

#Sreeti Ravi
#10/17/2020
#Question 1
#Write a program that creates a GUI window with following objects and their 
#functionalities:
#Two buttons, left and right, with colors different than the window background
#Mouse click on the left button changes the background color of a button for
#a short period (to indicate mouse click on the button) and increments a counter
#inside the button
#Mouse click on the right button changes the background color of a button for a
#short period (to indicate mouse click on the button), closes the window and 
#terminates the program


#I used code from Exercise 8.2 for this problem

from graphics import *

#delay
def delay(d):
    for i in range(d):
        for i in range(10000):
            pass

#returns True if point p is within rectangle rect and False otherwise    
def isButton(p, rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    if (p.getX() > p1.getX()) and (p.getX() < p2.getX()):
        if (p.getY() > p1.getY()) and (p.getY() < p2.getY()):
            return True
    return False
       
def main():
    #create a window
    win = GraphWin("",350,150)
    
    #Draw left button and text on the left button
    button_left = Rectangle(Point(50,40), Point(137.5,90))
    button_left.setFill('lightsteelblue')
    button_left.draw(win)
    
    text_left = Text(Point(93.75,65), "0")
    text_left.draw(win)
    
    #Draw right button and text on the right button
    button_right = Rectangle(Point(212.5,40), Point(300,90))
    button_right.setFill('lightsteelblue')
    button_right.draw(win)
    
    text_right = Text(Point(256.25,65), "Quit")
    text_right.draw(win)
    
    #initiate counter for left button
    counter_left = 0
    while True:
        pClick = win.getMouse()
        
        #if the right button clicked, break to terminate program
        if isButton(pClick, button_right):
            break
        
        #if left button clicked, change color of the left button
        elif isButton(pClick, button_left):
            button_left.setFill("grey")
            
            #delay
            delay(1000)
            
            #return button to original color
            button_left.setFill("lightsteelblue")
            
            #increment counter on the left button
            counter_left = counter_left + 1
            text_left.setText(counter_left)
    
    #close the window
    win.close()
    
main()