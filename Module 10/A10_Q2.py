# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 22:05:06 2020

@author: sreet
"""

#Sreeti Ravi
#10/31/2020
#Question 2
#Print company names and corresponding relative standard deviations

from pandas_datareader import data as web
import pandas as pd
import math

def rel_std(close):
    #average of all stock close values in 2020
    avg = close.sum() / len(close)
    
    #variance
    var = ((close - avg) ** 2).sum() / (len(close) - 1)
    
    #standard deviaiton of the stock close values
    std_dev = math.sqrt(var)
    
    #calculating relative standard deviation
    rel_std = (std_dev / avg) * 100
    
    return rel_std
    

def main():
    symbols = {"ba":'Boeing', "ko":'Coca Cola', "xom":'Exxon', "ge":'Mobil General Electric',
               "jpm":'JP Morgan' , "nke":'Nike', "pfe":'Pfeizer', "vz":'Verizon'}
    
    st_devs = {}
    
    for s in symbols:
        df = web.DataReader(s, "yahoo", '1/1/2020', '10/23/2020')
        close = rel_std(df["Close"])
        print(symbols[s], ":", round(close, 2))
        
main()