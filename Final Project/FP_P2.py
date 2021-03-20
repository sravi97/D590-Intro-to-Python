# -*- coding: utf-8 -*-

#Sreeti Ravi
#11-13-2020
#Final Project Phase 2
#Implementing k-means algorithm using initialization, assignment and recalculation



import pandas as pd
import numpy as np
import math as math

def main():
    #load dataset into Panda and find missing values
    df = pd.read_csv("breast_cancer_wisconsin.csv", na_values = ["?"])
    df.fillna(df.mean())
    
    #remove first and/or last rows
    data = list(df.columns)[1:10]

    #initialization: two random rows of data
    mu2_list = df[data].sample(1).values
    # print(mu2_list)

    mu4_list = df[data].sample(1).values
    # print(mu4_list)
    
    for i in range(15):
        #sum of the columns and square of the sum
        total_mu2 = np.sum((df[data] - mu2_list) ** 2, axis = 1)
        total_mu4 = np.sum((df[data] - mu4_list) ** 2, axis = 1)
        # print(total_mu2)
        # print(total_mu4)

        df['dist_mu2'] = np.sqrt(total_mu2)
        df['dist_mu4'] = np.sqrt(total_mu4)
        # print(df['dist_mu2'])
        # print(df['dist_mu4'])
        
        df.loc[df['dist_mu2'] <= df['dist_mu4'], 'Predicted'] = '2'
        df.loc[df['dist_mu2'] > df['dist_mu4'], 'Predicted'] = '4'
        
        avg = df[data + ['Predicted']].groupby(['Predicted']).mean()
        
        orig_mu2 = mu2_list
        orig_mu4 = mu4_list
        
        #replaces the old mu's with the new mu's
        mu2_list = list(avg.iloc[0,:])
        mu4_list = list(avg.iloc[1,:])

        if (list(orig_mu2) == mu2_list) and (list(orig_mu4) == mu4_list):
            break 
        
    print("------------Final Mean-----------------")
    print(avg)
    print("---------------Cluster Assignment")
    print(df[["scn","class","Predicted"]].head(20))


main()