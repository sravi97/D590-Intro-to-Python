#Sreeti Ravi
#11/8/2020
#Question 3
#Use numpy and matplotlib to produce a plot of the function f(x) = e−x/p sin(πx)
#over the interval [0, 10], for the values of the parameter p = 1, 2, 5. Include
#name of the plot, labels for the x- and y-axes, and a legend that identifies
#the lines by their color.

import matplotlib.pyplot as plt
import numpy as np
import math as math


def main():
    #set a figure and title
    fig = plt.figure()
    fig.suptitle("Function f(x) = exp(-x/p)sinx(pi x), p = 1, 2, 5")
    
    #set x and y labels
    plt.xlabel("x")
    plt.ylabel("f(x)")
    
    #create array x
    x = np.arange(0., 10., 0.1)
    
    #list of parameter values
    parameters = [1, 2, 5]
    
    #plot lines
    for p in parameters:
        #function
        y = np.exp(-x/p) * np.sin(np.pi * x)
        plt.plot(x, y, label = "p=" + str(p))
    
    #legend
    plt.legend(bbox_to_anchor = (0.675, 1), loc=2, borderaxespad = 0.) 

main()             