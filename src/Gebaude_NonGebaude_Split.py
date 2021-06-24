#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 23:38:22 2021

@author: khazi
"""
import nltk

def Gebaude_NonGebaude_Split(df):
   
    gebaude_rows = []
    non_gebaude_rows = []
    GebaudeNames = ['Gebäude', 'Geb', 'Geb.', 'Bau', 'BAU'] 

    gebäudeDict = {}

    sentArray = []
    xtense = df['Messstellenbezeichnung']
    for text in xtense:
        sentArray.append(text)

    bagWords = []
    for text in sentArray:
        temp = nltk.word_tokenize(str(text))
        bagWords.append(temp)

    for idx, row in enumerate(bagWords):
        flag = 0
        for keyWord in GebaudeNames: 
            if keyWord in row:
                gebaude_rows.append(idx)
                flag=1
        if flag==0:
            non_gebaude_rows.append(idx)
    
    df_gebaude_rows_only = df.iloc[gebaude_rows,:]
    df_non_gebaude_rows_only = df.iloc[non_gebaude_rows,:]
    
    
    
    return df_gebaude_rows_only,df_non_gebaude_rows_only