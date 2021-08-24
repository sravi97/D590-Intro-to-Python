# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 17:11:09 2020

@author: sreet
"""
#Sreeti Ravi
#10/17/2020
#Question 2
#Write a program that uses a graphical user interface (GUI) to calculate body
#mass index(BMI). the GUI window should have two objects for entering the height
#in inches and weight in pounds, a text object for displaying BMI and two buttons:
#Click on "Calculate BMI" button reads user inputs, calculates and displays BMI
#Click on "Quit" button closes the window and terminates the program

#I used code from Exercise 8.3 and my code for the BMI calculator
#from Assignment 6, Question 2 for this question

from graphics import *

def do_work(in_height, in_weight, BMI_number):
    
    #exception handling for height
    try:
        height = eval(in_height.getText())
    except:
        BMI_number.setText("Error!")
        return
    
    #exception handing for weight
    try:
        weight = eval(in_weight.getText())
    except:
        BMI_number.setText("Error!")
        return
    
    #checking if the height and weight are greater than 0
    if (height < 0) or (weight < 0):
        BMI_number.setText("Error!")
        return
    
    #converting height and weight to appropriate units
    height = height * 0.0254
    weight = weight * 0.453592
    
    #Calculates BMI
    BMI = weight / (height ** 2)
    
    #rounding BMI to fit in the box
    BMI_number.setText(round(BMI, 1))
    
def isButton(p, rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    
    #returns True if point p is within rectangle rect and False otherwise
    if (p.getX() > p1.getX()) and (p.getX() < p2.getX()):
        if (p.getY() > p1.getY()) and (p.getY() < p2.getY()):
            return True
    return False

#delay       
def delay(d):
    for i in range(d):
        for i in range(10000):
            pass


def main():
    #create window
    win = GraphWin("BMI Calculator", 470,230)
    
    #Draw left button and text on the left button
    button_calculate = Rectangle(Point(90,160), Point(200,200))
    button_calculate.setFill('lightsteelblue')
    button_calculate.draw(win)
    Text(Point(145,180), "Calculate BMI").draw(win)
    
    #Draw right button and text on the right button
    button_quit = Rectangle(Point(290,160), Point(360,200))
    button_quit.setFill('pink')
    button_quit.draw(win)
    Text(Point(325,180), "Quit").draw(win)
    
    #Create the text for each box
    Text(Point(220,50), "Your height in inches:").draw(win)
    Text(Point(216,80), "Your weight in pounds:").draw(win)
    Text(Point(233,110),"          Your BMI is:").draw(win)
    
    #create entry box for height
    in_height = Entry(Point(330,50), 5)
    in_height.setFill("white")
    in_height.draw(win)
    
    #create entry box for weight
    in_weight = Entry(Point(330,80), 5)
    in_weight.setFill("white")
    in_weight.draw(win)
    
    #Create box that displays BMI
    Rectangle(Point(305,100), Point(355, 120)).draw(win)
    BMI_number = Text(Point(330, 110), " ")
    BMI_number.draw(win)
    
    while True:
        pClick = win.checkMouse()
        if pClick:
            #if click is in right button, quit
            if isButton(pClick, button_quit):
                break
            
            #if click is on left button, calculate BMI
            elif isButton(pClick, button_calculate):
                button_calculate.setFill("grey")
                delay(1000)
                button_calculate.setFill("lightsteelblue")
                do_work(in_height, in_weight, BMI_number)
    
    #close window
    win.close()
    
main()
