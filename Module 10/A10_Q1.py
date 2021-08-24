# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:05:06 2020

@author: sreet
"""
#Sreeti Ravi
#10/31/2020
#Question 1
#Use pandas to download IBM stock data for year 2020 into a DataFrame, calculate
#and print the variance of close values using the formula. Find and print max 
#and min closing stock values and the respective dates.

from pandas_datareader import data as web
import pandas as pd
import math

def main():
    #download IBM stock data for year 2020 into a dataframe
    df_IBM = web.DataReader('ibm', 'yahoo', '1/1/2020', '10/23/2020')
    
    #dimensions of the DataFrame
    m, n = df_IBM.shape
    
    #average of all stock close values in 2020
    avg = df_IBM["Close"].sum() / m
    
    #variance
    var = ((df_IBM["Close"] - avg) ** 2).sum() / (m - 1) 
    
    #standard deviaiton
    st_dev = math.sqrt(var)
    
    #min closing stock values and the respective dates
    closing_min = df_IBM["Close"].min()
    date_min = df_IBM["Close"].idxmin()
    
    #max closing stock values and the respective dates
    closing_max = df_IBM["Close"].max()
    date_max = df_IBM["Close"].idxmax()
    
    
    print("Company: IBM  Year: 2020   Days:", m)
    print("\nAverage:", round(avg, 2))
    print("Variance:", round(var, 2))
    print("Standard Deviation:", round(st_dev, 2))
    print("\nLow:\t", date_min.date(), "\t", round(closing_min, 2))
    print("High:\t", date_max.date(), "\t", round(closing_max, 2))
    
          
    
main()
    