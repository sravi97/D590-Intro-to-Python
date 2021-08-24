# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 01:12:54 2020

@author: sreet
"""

#Sreeti Ravi
#10/10/2020
#Question 2
#Program to sum the rows of an input matrix

def input_matrix():
    #prompts the user for the dimension rows
    rows = input("Enter the number of rows: ")
    
    #exception handling for rows
    try:
        rows = int(rows)
    except ValueError:
        print("Error! Please enter a valid integer.")
        return
    
    #prompts the user for the dimension columns    
    columns = input("Enter the number of columns: ")
    
    #exception handling for columns
    try:
        columns = int(columns)
    except ValueError:
        print("Error! Please enter a valid integer.")
        return
    
    matrix = []
    #Prompts the user to enter integers and inserts into the list matrix
    for i in range(0, rows):
        row = []
        for j in range(0, columns):
            element = input(f"Enter next element of row {i}: ")
            try:
                element = int(element)
            except ValueError:
                print("Error! Please enter a valid integer.")
                return
            row.append(element)
        matrix.append(row)
    return matrix
    
def print_matrix(matrix):
    #prints each row in a spearate line, with no square brackets
    for i in range(0, len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=("\t"))
        print()

#sums the columns of the matrix and put results into a list    
def sum_columns(matrix):
    sums = []
    for j in range(len(matrix[0])):
        sum = 0
        for i in range(0, len(matrix)):
            sum = sum + matrix[i][j]
        sums.append(sum)
    return sums
    
def main():
    #Calls function input_matrix() to get a matrix from the user
    print("Programm prints min, max, and count of positive and negative numbers")
    matrix = input_matrix()
    
    #Calls function print_matrix(matrix) to print the input matrix
    print("\nInput matrix:")
    print_matrix(matrix)
    
    #Calls function sum_columns(matrix) to sum the columns of the input matrix and
    #prints the sums of columns of the input matrix as a list
    sums = sum_columns(matrix)
    print("\nThe sum of the columns are:")
    print(sums)   
    
main()