# -*- coding: utf-8 -*-

#Sreeti Ravi
#12-01-2020
#Final Project Phase 3
#Calculate the individual and total error rate of your 2 clusters


import pandas as pd
import numpy as np

def main():
    #load dataset into Panda and find missing values
    df = pd.read_csv("breast_cancer_wisconsin.csv", na_values = ["?"])
    
    #Fill missing values with mean
    df.fillna(df.mean())
    
    #remove first and/or last rows
    data = list(df.columns)[1:10]
    
    #choose two random datapoints for mu2 and mu4
    mu2_list = df[data].sample(1).values
    # mu2_list = df[data][5:6]
    print('mu2: ', mu2_list)

    mu4_list = df[data].sample(1).values
    # mu4_list = df[data][245:246]
    print('mu4: ', mu4_list)
    
    
    for i in range(15):
        #sum of the columns and square of the sum
        total_mu2 = np.sum((df[data] - mu2_list) ** 2, axis = 1)
        total_mu4 = np.sum((df[data] - mu4_list) ** 2, axis = 1)
        # print(total_mu2)
        # print(total_mu4)
        
        #square root of row totals
        df['dist_mu2'] = np.sqrt(total_mu2)
        df['dist_mu4'] = np.sqrt(total_mu4)
        # print(df['dist_mu2'])
        # print(df['dist_mu4'])
        
        #assign datapoint to cluster 2 if mu2 distance is smaller
        #assign to cluser 4 otherwise
        df.loc[df['dist_mu2'] < df['dist_mu4'], 'Predicted_Class'] = '2'
        df.loc[df['dist_mu2'] >= df['dist_mu4'], 'Predicted_Class'] = '4'
        
        avg = df[data + ['Predicted_Class']].groupby(['Predicted_Class']).mean()
        
        #replace the old mu's with the new mu's
        orig_mu2 = mu2_list
        orig_mu4 = mu4_list
        
        mu2_list = list(avg.iloc[0,:])
        mu4_list = list(avg.iloc[1,:])
                
        #break if cluster assignments don't change
        if (list(orig_mu2) == mu2_list) and (list(orig_mu4) == mu4_list):
            break 
        
    # print("--------------------------Final Mean---------------------------------")
    # print(mu2_list)
    # print(mu4_list)
    
    # print("--------------------------Cluster Assignment---------------------------------")
    # print(df[["scn","class","Predicted_Class"]].head(21))
    
    #variable to store all necesary columns
    columns = df[["scn","class","Predicted_Class"]]
    
    predicted_class = list(columns.iloc[:,2])
    actual_class = list(columns.iloc[:,1])
    
    # print(predicted_class)
    # print(actual_class)
    
    #initiate variables for counting errors
    count_2 = 0
    count_4 = 0
    
    for i in range(len(predicted_class)):
        #error B numerator
        if predicted_class[i] == '4' and actual_class[i] == 2:
            count_2 += 1
        
        #error M numerator 
        elif predicted_class[i] == '2' and actual_class[i] == 4:
            count_4 += 1
    
         
    predicted_2 = 0
    predicted_4 = 0
    actual_2 = 0
    actual_4 = 0
    
    #count actual and predicted data
    for i in range(len(predicted_class)):
        if predicted_class[i] == '2':
            predicted_2 += 1
            
        elif predicted_class[i] == '4':
            predicted_4 += 1
            
    for i in range(len(actual_class)):        
        if actual_class[i] == 2:
            actual_2 += 1
            
        elif actual_class[i] == 4:
            actual_4 += 1
    
    #calculate error B and error M
    error_B = count_2 / predicted_2
    error_M = count_4 / predicted_4
    
    print("\n\t\t\tBenign \t\tMalign")
    print("Predicted   ", predicted_2, "\t\t", predicted_4)
    print("Actual      ", actual_2, "\t\t", actual_4)
    
    print("\nActual malignant samples classified as benign: ", count_4)
    print("Actual benign samples classified as malignant: ", count_2)
    
    print("\nError B: ", error_B)
    print("Error M: ", error_M)
    
    total_error = (count_2 + count_4) / (predicted_2 + predicted_4)
    print("\nTotal Error: ", total_error)
    
main()