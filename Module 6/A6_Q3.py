# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 22:07:27 2020

@author: sreet
"""

#Sreeti Ravi
#10-03-20
#Assignment 6
#Question 3
# Write function point() that prompts the user for a player who
# wins a point and returns “A” if player A wins a point and returns
# “B” if player B wins a point, and returns "E" is use enters anything else.
# Write function game() that keeps the score in the game and returns
# “A” if player A wins the game or “B” if player B wins the game.

def point():
    #Gets input from user 
    player = input("Who wins a point, player A or B? ")
    if player.upper() == 'A':
        return 'A' 
    elif player.upper() == 'B':
        return 'B' 
    else:
        print("Error: Invalid input")
        return 'E'


#Write function game() that keeps the score in the game and returns
#“A” if player A wins the game or “B” if player B wins the game.
def game():
    # setting up variables for scores and setting them to zero
    a_score = 0
    b_score = 0 
    # define a for loop that will work long enogh to cover the worst case scenario
    for i in range(16):
    # inside the for loop set up conditionals tp check if someone wins and return the proper value
        player = point()    
        if player == 'A':
            a_score += 1
        elif player == 'B':
            b_score += 1

        #Prints score every time user enters who wins the game
        print("A Score: ", a_score)  
        print("B Score: ", b_score)      
            
        if a_score >= 3 and (a_score - b_score) >= 2:
            return 'A'
        elif b_score >= 3 and (b_score - a_score) >= 2:
            return 'B'
        elif a_score >= 7 and a_score >= b_score:
            return 'A'
        elif b_score >= 7 and b_score >= a_score:
            return 'B'

# main
def main():
# define your main() function here that has a docstring describing what this program does
    """Calls game() to determine the winner of the game """
    print("The program keeps score in a game.")
# finds the winner
    winner = game()
# prints the result
    print("\n\nThe winner is player", winner, "!")
main()