# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 19:42:55 2020

@author: sreet
"""

#Sreeti Ravi
#Final Project Phase 1

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def main():
    #load dataset into Panda and find missing values
    df = pd.read_csv("breast_cancer_wisconsin.csv", na_values = ["?"])
    df.fillna(df.mean())
    
    #creating lists to index in for loop 
    columns = ['scn','a2','a3','a4','a5','a6','a7','a8','a9','a10','class']
    titles = ["Sample Code Number: ID Number", "Clump Thickness: 1- 10", \
              "Uniformity of Cell Size: 1-10", "Uniformity of Cell Shape: 1-10", \
              "Marginal Adhesion: 1-10", "Single Epithelial Cell Size: 1-10", \
              "Bare Nuclei: 1-10", "Bland Chromatin: 1-10", "Normal Nuclei: 1-10", \
              "Mitoses: 1-10", "Cell Type: 2 (benign) or 4(malignant)"]
    
    #initialize index
    i = 0
    for column in columns:
        #set a figure and subplot
        fig_a1 = plt.figure()
        sp1 = fig_a1.add_subplot(1, 1, 1)
        
        #set a title
        sp1.set_title(titles[i])
        
        #set x and y axis labels
        sp1.set_xlabel("Value of the attribute")
        sp1.set_ylabel("Number of data points")
        
        #draw histogram
        sp1.hist(df[column], bins=10, color = "orange", edgecolor="black", \
                  linewidth=1.2, alpha = 0.5)
        
        i += 1
        
        #compute and print data statistics
        print("\nAttribute", i,"-----------")
        print("Mean:", np.around(df[column].mean(), decimals = 1))
        print("Median:", np.around(df[column].median(), decimals = 1))
        print("Variance:", np.around(df[column].var(), decimals = 1))
        print("Standard Deviation:", np.around(df[column].std(), decimals = 1))
    
    
main()