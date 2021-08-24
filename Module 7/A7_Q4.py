# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 01:12:55 2020

@author: sreet
"""

#Sreeti Ravi
#10/10/2020
#Question 4
#Program keeps a score and prints winner in a tennis game

def point():
    #Prompts the user for the player who wins a point
    winner = input("Who wins a point, player A or B? ")
    
    #Returns "A" if the user enters "A" or "a" to indicate that player A wins
    if winner.upper() == 'A':
        return 'A'
    
    #Returns "A" if the user enters "B" or "b" to indicate that player B wins
    elif winner.upper() == 'B':
        return 'B'
    
    #Returns "Q" if the user enters "Q" or "q" to quit the program
    elif winner.upper() == 'Q':
        return 'Q' 
    
    #Returns "E" if user enters anything else
    else:
        return 'E'
    
def game():
    score_a = 0
    score_b = 0
    play = True
    
    while play: 
        #Calls function point() to get input from the user
        winner = point()    
        #Increments score of player A if point() returns "A"
        if winner == 'A':
            score_a += 1
            
        #Increments score of player B if point() returns "B"
        elif winner == 'B':
            score_b += 1
        
        #Quits the program if point() returns "Q"
        elif winner == 'Q':
            print("You quit the game.")
            play = False
       
        #Prints error message if point() returns "E"
        elif winner == 'E':
            print("Invalid input. Please enter A, B or Q (to quit). ")
            
        #If game is over, prints and winner and returns to main(), which terminates to program
        if score_a >= 4 and (score_a - score_b) >= 2:
            print("Player A wins the game.")
            play = False
            
        elif score_b >= 4 and (score_b - score_a) >= 2:
            print("Player B wins the game.")
            play = False
            
            
        #Prints score every time user enters who wins the game
        if play:
            display(score_a, score_b)      
    
def display(score_a, score_b):
    
    #deuce if both players have at least 3 points and same number of points
    #After a deuce, the score for the player who has 1 more point is 
    #displayed as “Adv” and the score of the other players as “ “
    if score_a >= 4 and score_a > score_b:
        score_a = "Adv"
        score_b = ""
    elif score_b >= 4 and score_b > score_a:
        score_a = ""
        score_b = "Adv"
    elif score_a >= 4 and score_b >= 4 and score_a == score_b:
        score_a = 40
        score_b = 40    
    
    #mapping of the first 3 points to displayed values
    if score_a == 1:
        score_a = 15
    elif score_a == 2:
        score_a = 30
    elif score_a == 3:
        score_a = 40
    
    if score_b == 1:
        score_b = 15
    elif score_b == 2:
        score_b = 30
    elif score_b == 3:
        score_b = 40
    
    #print scores
    print("A Score: ", score_a)  
    print("B Score: ", score_b) 
    

def main(): 
    game()
    
main()