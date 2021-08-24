# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:11:10 2020

@author: sreet
"""

#Sreeti Ravi
#10/17/2020
#Question 3
#Write a program that creates a window with a circle that bounces from the 
#window walls.

#I used code from Exercise 8.7 from this question

from graphics import *

#delay
def delay(m):
    for i in range(m):
        for i in range(10000):
            pass

def main():
    #create a window
    win = GraphWin("", 500, 300)
    r = 20
    
    #draw a circle
    p1 = Point(250, 150)
    circ = Circle(p1, r)
    circ.setFill('yellow')
    circ.draw(win)
    
    dx = 1
    dy = 1
    
    while True:
        #move circle by dx and dy
        circ.move(dx, dy)
        
        #delay
        delay(50)
        
        p = circ.getCenter()
        #if circle hits a vertical wall set change x direction
        if ((p.getX() - r) <= 0) or ((p.getX() + r) >= 500 ):
            dx = -dx
        
        #if circle hits a horizontal wall change y direction
        if ((p.getY() - r) <= 0) or ((p.getY() + r) >= 300):
            dy = -dy
        
        #break if the user terminates the program
        key = win.checkKey()
        if key == "q":
            break
        
    #close the window
    win.close()
    
main()
        