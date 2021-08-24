# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:57:43 2020

@author: sreet
"""

#Exercise 11.1
#Copy box office data for year 2019 into Excel file "Movies_2019.xlsx". 
#Write a Python program that uses pandas and matplotlib to:
    #Read Excel file "Movies_2019.xlsx" with 2019 movie data,
    #Keep the first 100 rows, discard the rest of the DataFrame,
    #Print histogram of total gross with 20 bins
#Include labels for the horizontal and vertical axes and the names of plots

# import matplotlib.pyplot as plt
# import pandas as pd

# def main():
#     #read Excel file
#     xls_file = pd.ExcelFile("Movies_2019.xlsx")
    
#     #parse the Excel sheet "2019", store data into DataFrame movies
#     movies = xls_file.parse("2019")

#     #set index 
#     movies.index = range(len(movies))

#     #take Gross of the top 100 movies
#     gross = movies[:100][["Gross"]]
    
#     #represent Gross in million
#     gross["Gross"] = gross["Gross"] / 100000000
#     print(gross)
    
#     #plot the historgram
#     fig1 = plt.figure()
#     sp1 = fig1.add_subplot(1,1,1)
#     sp1.set_title("Histogram of total gross")
#     sp1.set_xlabel("Total gross (million of $)")
#     sp1.set_ylabel("Number of movies")
#     sp1.hist(gross["Gross"], bins=20, color="green", edgecolor='black', \
#               linewidth=1.2, alpha=0.5)
        
# main()

#Exercise 11.2
#Write a program that imports data from Excel file "Movies_2019.xlsx" and uses
#matplotlib to draw a scatter plot of "Gross" versus "Opening" gross
#Include name of the plot and labels for the x- and y- axes.

# import matplotlib.pyplot as plt
# import pandas as pd

# def main():
#     #read Excel file
#     xls_file = pd.ExcelFile("Movies_2019.xlsx")
    
#     #parse the file
#     movies = xls_file.parse("2019")
    
#     #set index
#     movies.index = range(len(movies))
    
#     #gross and oepning of the top 100 movies
#     movies_100 = movies[:100][["Gross", "Opening"]]
    
#     movies_100["Gross"] = movies_100["Gross"] / 10000000
#     movies_100["Opening"] = movies_100["Opening"] / 10000000
    
#     fig = plt.figure()
#     fig.suptitle("Total vs. Opening Gorss [in millions of $]", fontsize = 12)
    
#     #set x and y labels
#     plt.xlabel("Opening")
#     plt.ylabel("Total Gross")
    
#     #scatter plot
#     plt.scatter(movies_100["Opening"], movies_100["Gross"], color="blue", \
#                 alpha = 0.5)

# main()

#Exercise 11.3
#Write a program that uses matplotlib to draw function f = sin(x + phi) over
#interval (o, 2pi)for parameter phi = 0, pi/4, pi/2, 3pi/4. Include name of the
#plot, labels for the x- and y-axes, and a legend that identifies the lines by
#their color

import matplotlib.pyplot as plt
import numpy as np
import math as math

def main():
    #set a figure and title
    fig = plt.figure()
    fig.suptitle("Function f(x) = sin(x + phi), phi = 0, pi/4, pi/2, 3pi/4")
    
    #set x and y labels
    plt.xlabel("x")
    plt.ylabel("f(X) = sin(x + phi)")
    
    #create array x
    x = np.arange(0., 10, 0.1)
    
    #list of parameter values
    phi = [1, 2, 5]
    
    #plot lines
    #use i to create labels
    # i = 0
    for p in phi:
    #     #create label
    #     if i == 0:
    #         lab = "p=0"
    #     elif i == 1:
    #         lab = "p=pi/4"
    #     else:
    #         lab = "p=" + str(i) + "pi/4"
        plt.plot(x, np.exp(-x/p) * np.sin(np.pi * x), label = "p=" + str(p))
    
    #Place a legend to the right of the plot
    plt.legend(bbox_to_anchor=(0.675, 1), loc=2, borderaxespad=0.)
    
main()

#Exercise 11.4
#Draw a parametric function of a parameter t, 0 <= t < 12*pi, given by:
    #x = cos(t) - 3 + t/2*pi
    #y = sint(t)
    
# import matplotlib.pyplot as plt
# import numpy as np
# from math import pi

# def main():
#     #set a figure and title
#     fig = plt.figure()
#     fig.suptitle("Function x=cos(t)-3+t/(2*pi), y=sin(t)", fontsize=12)
    
#     #set x and y labels
#     plt.xlabel("x = cos(t) - 3 + t/(2*pi)")
#     plt.ylabel("y = sint(t)")
    
#     #create array x
#     t = np.arange(0., 12*pi, 0.1)
    
#     x = np.cos(t) - 3 + t/(2*pi)
#     y = np.sin(t)
    
#     #set limits for y axis 
#     axes = plt.gca()
#     axes.set_ylim([-3, 3])
    
#     plt.plot(x, y)
    
# main()


