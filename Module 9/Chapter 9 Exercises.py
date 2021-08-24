# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 20:19:18 2020

@author: sreet
"""

# ex_9_4.py
# Tip statistics.
# import numpy as np
# from numpy import genfromtxt
# def main():
#  # row 0: headings
#  # column 0: total bill
#  # column 1: tip
#  # column 2: sex (0 female, 1, male)
#  # column 3: day (1 Sunday, 5 Thursday, 6 Friday, 7 Saturday)
#  # column 4: party size

#  # read data from csv file
#      t = genfromtxt("tips.csv", delimiter = ",")
#      tips = t[1:] # drop the heading row
#      m, n = tips.shape
#      print("\nStatistics on ", m, "tips.")
#      print(tips)
     
# main()


import numpy as np
from numpy import genfromtxt
def main():
    print("\nProgram that finds a year with min and max inflation rate.")
 # suppress scientific notation
    np.set_printoptions(suppress=True)

 # row 0: headings
 # column 0: year
 # column 1: quarter
 # column 12: quarterly inflation rate

 # read data from csv file
    macro = genfromtxt("MacroData.csv", delimiter = ",")

 # select columns with year, quarter and inflation rate with fancy indexing
 # drop the headings
    infl = macro[1:, [0, 12]]
 # infl columns:
 # 0: year
 # 1: quarterly inflation rate
 # print(infl)

 # yearly inflation rate
    m, n = infl.shape
    print (m,n)
    print(infl.shape)
    year_infl = infl.reshape(int(m/4), 8)
    print(year_infl)
 # use fancy indexing to extract year and inflation rates
    year_infl = year_infl[:, [0, 1, 3, 5, 7]]
 # print(year_infl)

    year_rate = np.zeros([int(m/4), 2])
    year_rate[:, 0] = year_infl[:, 0]
    year_rate[:, 1] = year_infl[:, 1:].sum(axis = 1) / 4
    
    print("\n Year Inflation (%)")
    print(year_rate)

 # lowest inflation rate
    i = np.argmin(year_rate[:, 1])
    print("The lowest inflation ", year_rate[i, 1], "was in ", int(year_rate[i, 0]))
 # highest inflation rate
    j = np.argmax(year_rate[:, 1])
    print("The highest inflation ", year_rate[j, 1], "was in ", int(year_rate[j, 0]))

main()