# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:05:08 2020

@author: sreet
"""

#Sreeti Ravi
#10/31/2020
#Question 4
#Finds the maximum period in which the close value of the stock was up each day

from pandas_datareader import data as web

def max_up(stock):
    #initializing variables
    days_up = 0
    max_period = 0
    start_period = 0
    
    #finding the longest period
    for i in range(1, len(stock)):
        if stock["Close"][i] > stock["Close"][i-1]:
            days_up += 1
        else:
            if days_up > max_period:
                max_period = days_up
                start_period = i - max_period
            days_up = 0
    
    return start_period, days_up, max_period

def main():
    #prompt the user for the stock symbol
    stock_symbol = input("Symbol: ")
    
    #download stock data for 2020 into a DataFrame
    df = web.DataReader(stock_symbol, "yahoo", '1/1/2020', '10/23/2020')
    
    #call function max_up(stock)
    start_period, days_up, max_period = max_up(df)
    
    #number of days 
    print("Days:", max_period)
    
    start_date = df["Close"].index[start_period]
    print("\nStart:", start_date.date())
    
    start_value = df["Close"][start_date]
    print("Close:", round(start_value, 2))
    
    end_date = df["Close"].index[start_period + max_period - 1]
    print("\nEnd:", end_date.date())
        
    end_value = df["Close"][end_date]
    print("Close:", round(end_value, 2))
        
main()