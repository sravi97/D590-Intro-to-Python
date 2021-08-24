# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:05:06 2020

@author: sreet
"""

#Sreeti Ravi
#10/31/2020
#Question 3
#Print the sample correlation between the close values of two companies

from pandas_datareader import data as web
import pandas as pd
import math

def cor(stock_ba, stock_ko):

    #average of all stock close values in 2020
    avg_ba = stock_ba.sum() / len(stock_ba)
    avg_ko = stock_ko.sum() / len(stock_ko)
    
    #variance
    var_ba = ((stock_ba - avg_ba) ** 2).sum() / (len(stock_ba) - 1)
    var_ko = ((stock_ko - avg_ko) ** 2).sum() / (len(stock_ko) - 1)

    #standard deviaiton of each stock close values
    std_dev_ba = math.sqrt(var_ba)
    std_dev_ko = math.sqrt(var_ko)

    
    #calculating sample covariance
    cov = ((stock_ba - avg_ba) * (stock_ko - avg_ko)).sum() / (len(stock_ba) - 1)
    
    correlation = cov / (std_dev_ba * std_dev_ko)
    # cor_value = cov/denom

    return avg_ba, avg_ko, std_dev_ba, std_dev_ko, correlation
    

def main():
    #download Boeing and Coca-Cola stock data for 2020
    df_ba = web.DataReader("ba", "yahoo", '1/1/2020', '10/23/2020')
    df_ko = web.DataReader("ko", "yahoo", '1/1/2020', '10/23/2020')
    
    stock_ba = df_ba["Close"]
    stock_ko = df_ko["Close"]
    
    avg_ba, avg_ko, std_dev_ba, std_dev_ko, correlation = cor(stock_ba, stock_ko)
    
    print("Company: Boeing")
    print("Symbol: BA")
    print("\nAverage:", round(avg_ba, 2))
    print("Standard Deviation:", round(std_dev_ba, 2))
    
    print("\nCompany: Coca-Cola")
    print("Symbol: KO")
    print("\nAverage:", round(avg_ko, 2))
    print("Standard Deviation:", round(std_dev_ko, 2))
    
    print("\nCorrelation:", round(correlation, 2))
    

main()