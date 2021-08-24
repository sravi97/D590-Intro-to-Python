#Sreeti Ravi
#11/8/2020
#Question 2
#Use Pandas and matplotlib to produce a scatter plot of weights versus heights.
#Include the name of the plot and labels for the horizontal and vertical axes

import matplotlib.pyplot as plt
import pandas as pd

def main():
    #read the Excel file
    xls_file = pd.ExcelFile("heights_weights.xlsx")
    
    file = xls_file.parse("Sheet1")
    
    #set a figure and title
    fig = plt.figure()
    fig.suptitle("Scattered plot, weights vs. heights", fontsize = 12)
    
    #set x and y labels
    plt.xlabel("Heights")
    plt.ylabel("Weights")
    
    #scatter plot
    plt.scatter(file["Height"], file["Weight"], color="red")
    
main()
    
    