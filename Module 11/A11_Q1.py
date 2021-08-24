#Sreeti Ravi
#11/8/2020
#Question 1
#Reading data file and drawing two histograms 

import matplotlib.pyplot as plt
import pandas as pd

def main():
    #read Excel file with heights_weights into pandas dataframe
    xls_file = pd.ExcelFile("heights_weights.xlsx")
    
    #parse through the file
    file = xls_file.parse("Sheet1") 
    
    #histogram for heights 
    fig1 = plt.figure()
    sp1 = fig1.add_subplot(1, 1, 1)
    sp1.set_title("Histogram of heights")
    sp1.set_xlabel("Heights")
    sp1.set_ylabel("Number of students")
    sp1.hist(file["Height"], bins=16, color = "blue", edgecolor="black", \
              linewidth=1.2, alpha = 0.5)
    
    #histogram for weights
    fig2 = plt.figure()
    sp2 = fig2.add_subplot(1, 1, 1)
    sp2.set_title("Histogram of weights")
    sp2.set_xlabel("Weights")
    sp2.set_ylabel("Number of students")
    sp2.hist(file["Height"], bins=16, color = "red", edgecolor="black", \
             linewidth = 1.2, alpha = 0.5)

    
    
main()