# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:25:26 2020

@author: sreet
"""
#Exercise 8.1
#Write a program that accepts two mouse clicks of the opposite corners of a 
#rectangle. The program draws the rectangle, and prints the perimeter and area
#of the rectangle. Assume that 1 inch is approximately 90 points
# from graphics import *
# import math

# def main():
#     win = GraphWin("Rectangle!", 500, 500)
    
#     msg = Text(Point(250,400),"Click opposite corners of a rectange.").draw(win)
    
#     point1 = win.getMouse()
#     point1.draw(win)
#     point2 = win.getMouse()
#     point2.draw(win)
    
#     rect = Rectangle(point1, point2)
#     rect.setWidth(2)
#     rect.draw(win)
    
#     width = abs(point2.getX() - point1.getX())
#     height = abs(point2.getY() - point1.getY())
#     area = round(width * height / (90 * 90), 1)
#     perimeter = round(2 * (width + height) / 90, 1)
    
#     msg.setText("The perimeter is " + str(perimeter) + " inches.")
#     Text(Point(250,450),"The area is " + str(area) + " square inches.").draw(win)
    
#     win.getMouse()
#     win.close()
    
# main()

#Exercise 8.2
#Draw a window with two countdown buttons with fixed initial counter values. A
#mouse click on button decrements its couter. The program terminates when one
#of the counters decrements to 0

# from graphics import *

# def put_buttons(win):
#     button_left = Rectangle(Point(65,50), Point(235,100))
#     button_left.setFill('lightgrey')
#     button_left.draw(win)
    
#     text_left = Text(Point(150, 75), "3")
#     text_left.draw(win)
    
#     button_right = Rectangle(Point(265,50), Point(435,100))
#     button_right.setFill('lightgrey')
#     button_right.draw(win)
    
#     text_right = Text(Point(350, 75), "3")
#     text_right.draw(win)
    
#     return button_left, text_left, button_right, text_right
    
# def main():
#     win = GraphWin("Two buttons", 500, 300)
#     button_left, text_left, button_right, text_right = put_buttons(win)
#     msg = Text(Point(250, 200), "Click a button to decrement its couter").draw(win)
    
#     counter_left = 3
#     counter_right = 3
    
#     while True:
#         pt = win.getMouse()
#         if pt:
#             if 
                
# main()

#Exercise 8.3 
#Draw a window with two text "Your score in points:" and "Your letter grade:"
#and two buttons. When the user clicks the left button, the program reads score
#in points, calculates and displays the letter grade.
#In case of invalid input, program displays "error"
#Click on the right button terminates the program.
from graphics import *

def do_work(in_score, text_grade):
    try:
        score = eval(in_score.getText())
    except: # catch all exceptions
        text_grade.setText("Error!")
        return

    if (score > 100) or (score < 0): # score outside the range?
        text_grade.setText("Error!")
        return

    if (score >= 93):
        grade = 'A'
    elif (score >= 90):
        grade = 'A-'
    elif (score >= 86):
        grade = 'B+'
    elif (score >= 83):
        grade = 'B'
    elif (score >= 80):
        grade = 'B-'
    elif (score >= 76):
        grade = 'C+'
    elif (score >= 73):
        grade = 'C'
    elif (score >= 70):
        grade = 'C-'
    elif (score >= 66):
        grade = 'D+'
    elif (score >= 60):
        grade = 'D'
    else:
        grade = 'F'

    text_grade.setText(grade)

def is_button(click, rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    if (click.getX() > p1.getX()) and (click.getX() < p2.getX()):
        if (click.getY() > p1.getY()) and (click.getY() < p2.getY()):
            return True
    return False 

def delay(d):
    for i in range(d):
        for i in range(10000):
            pass # do nothing, just wait

def main():
    win = GraphWin("Letter grade calculator", 370, 230)
    
    button_do = Rectangle(Point(30, 130), Point(200, 170))
    button_do.setFill('lightgrey')
    button_do.draw(win)
    Text(Point(115,150), "Calculate letter grade").draw(win)
    
    button_quit = Rectangle(Point(230,120),Point(330,170))
    button_quit.setFill('lightgrey')
    button_quit.draw(win)
    Text(Point(280,150), "Quit program").draw(win)
    
    Text(Point(120,50), "Your score in points:").draw(win)
    Text(Point(120, 80), "  Your letter grade:").draw(win)
    
    in_score = Entry(Point(240,50), 5)
    in_score.setFill("white")
    in_score.setText(" 0")
    in_score.draw(win)
    
    Rectangle(Point(215,70), Point(265,90)).draw(win)
    text_grade = Text(Point(240, 80), " ")
    text_grade.draw(win)
    
    while True:
        pt = win.checkMouse()
        if pt:
            if is_button(pt, button_quit):
                break
            
            elif is_button(pt, button_do):
                button_do.setFill("grey")
                delay(1000)
                button_do.setFill("lightgrey")
                do_work(in_score, text_grade)
    win.close()
    
main()
    

# #Exercise 8.4
# from graphics import *

# def main():
#     win = GraphWin("10 Circles", 500, 300)
#     for i in range(10):
#         click = win.getMouse()
#         Circle(click, 30).draw(win)
#     win.getMouse()
#     win.close()
# main()

#Exercise 8.5
# ex_8_5.py: move a circle to the point of mouse click.
# from graphics import *
# from math import *

# def delay(m):
#     for i in range(m):
#         for i in range(10000):
#             pass # do nothing, just wait
# def main():
#     win = GraphWin("Moves a circle to the mouse click", 500, 300)
#     circle = Circle(Point(250,250), 20)
#     circle.setFill("pink")
#     circle.draw(win)

#     while(True):
#         pt = win.getMouse()
#         c = circle.getCenter()

#         # alpha is the angle to the point of the mouse click
#         if (pt.getX() - c.getX()) == 0: # mouse click is above
#             if (c.getY() - pt.getY()) >= 0: # or below the center of circle
#                 alpha = pi/2
#             else:
#                 alpha = - pi/2
#         else:
#             # calculate angle
#             alpha = atan((c.getY() - pt.getY()) / (pt.getX() - c.getX()))
    
#             # correction of the angle
#             if (pt.getX() - c.getX()) < 0:
#                 if (c.getY() - pt.getY()) >= 0:
#                     alpha = pi + alpha
#                 else:
#                     alpha = - pi + alpha
    
#         while True: # move circle to the point of click
#             circle.move(cos(alpha), - sin(alpha))
#             delay(50)
#             # move circle until its center is close to the point of mouse click
#             c = circle.getCenter()
#             if(abs(c.getX()-pt.getX()) <= 1) and (abs(pt.getY()-c.getY()) <= 1):
#                 break
    
#          # press "q" to quit
#         key = win.checkKey()
#         if key == "q": # loop exit
#             break
    
#     win.close()
# main()