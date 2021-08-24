# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:11:10 2020

@author: sreet
"""

#Sreeti Ravi
#10/17/2020
#Question 4
#Write a program that creates a circle at a random point in a window. If the 
#user clicks within the circle, it will disappear and the program draws a new
#circle at a random point
#If the user does not click on the circle within a specified time interval:
#the circle disappears 
#Appears a message "You missed the circle! Game over! Click mouse to close the
#window."
#The program terminates on next mouse click

#I used code from Exercise 8.8

from graphics import *
from random import randrange
from math import sqrt

#delay
def delay(d):
    for i in range(d):
        for i in range(10000):
            pass

def main():
    #create window
    height = 300
    width = 500
    r = 30
    win = GraphWin("Pop a circle", width, height)
    
    while True:
        #create a circle at a random point within the window
        center = Point(randrange(r, width -r), randrange(r, height - r))
        circ = Circle(center, r)
        circ.setFill('pink')
        circ.draw(win)
       
        #delay
        delay(60)
      
        #if there is a mouse click:
        click = win.getMouse()
        c = circ.getCenter()
        diameter = sqrt((c.getX() - click.getX())**2 + (c.getY() - click.getY())**2)
        
        
        if (diameter > r):
            circ.undraw()
            Text(Point(250, 80), "You missed the circle!").draw(win)
            Text(Point(250, 100), "Game Over! Click mouse to close the window.").draw(win)
            win.getMouse()
            win.close()
        else:
            circ.undraw()
        
main()