#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 21:37:04 2021

@author: khazi
"""

#from nltk.stem import PorterStemmer
#from nltk.corpus import stopwords
import nltk
import re
import numpy as np
import pandas as pd


def gebaudeExtract(df):
    
    df['Gebäude/Geb./Geb/Bau'] = " "
    
    GebaudeNames = ['Gebäude', 'Geb', 'Geb.', 'Bau'] 
    gebäudeDict = {}
    sentArray = []
    bagWords = []
    
    
    xtense = df['Messstellenbezeichnung']
    for text in xtense:
        sentArray.append(text)

    
    for text in sentArray:
        temp = nltk.word_tokenize(str(text))
        bagWords.append(temp)
    
   # only gebaued list
    for idx, row in enumerate(bagWords):
        flag = 0
        for keyWord in GebaudeNames: 
            if (keyWord in row) and flag==0:
                if row[-1]== keyWord:
                    flag = 1
                    temp = keyWord + " NaN"
                    gebäudeDict[idx] = temp 
                else:
                    flag = 1
                    index = row.index(keyWord)
                    
                    if row[index+1].isnumeric():
                        temp = keyWord + ' ' + row[index+1]
                    elif ',' in row[index+1]:
                        temp = re.split(',', row[index+1])
                        temp = keyWord + ' ' + temp[0]
                    else:
                        temp = np.NaN
                    
                    gebäudeDict[idx] = temp 
                    
                    
                    #temp = keyWord + ' ' + row[index+1]
                    #gebäudeDict[idx] = temp                

        if flag==0:
            temp = np.NaN #keyWord + " NaN"
            gebäudeDict[idx] = temp
        
    
    for index, name in gebäudeDict.items():
        df['Gebäude/Geb./Geb/Bau'][index] = name

    
    return df




def NonGebaudeExtract(df):
    nonGebaudeNames = ['Fuel', 'Station', 'Bürocontainer', 'Süd', 'Container']
    df['Stat/Fuel/Container/Süd'] = " "

    nonGebäudeDict = {}
    sentArray = []
    
    xtense = df['Messstellenbezeichnung']
    for text in xtense:
        sentArray.append(text)

    bagWords = []
    for text in sentArray:
        temp = nltk.word_tokenize(str(text))
        bagWords.append(temp)
    
   #
    # non gebaued list
    for idx, row in enumerate(bagWords):
        flag = 0
        for keyWord in nonGebaudeNames: 
            if (keyWord in row) and flag==0:
                if row[-1]== keyWord:
                    flag = 1
                    temp = np.NaN
                    nonGebäudeDict[idx] = temp 
                else:
                    flag = 1
                    index = row.index(keyWord)
                    if row[index+1].isnumeric():
                        temp = keyWord + ' ' + row[index+1]
                    else:
                        temp = np.NaN
                    
                    nonGebäudeDict[idx] = temp                

        if flag==0:
            temp = np.NaN
            nonGebäudeDict[idx] = temp
    
    
    for index, name in nonGebäudeDict.items():
        df['Stat/Fuel/Container/Süd'][index] = name
    
    return df


def gebaude_only(df):
    
    df3_gebaude = df.copy()
    for i, text in enumerate(df3_gebaude['Gebäude/Geb./Geb/Bau']):
        if pd.isna(text):
            df3_gebaude = df3_gebaude.drop(i)
        elif text.split()[0] == "Gebäude":
            pass
        else:
            df3_gebaude = df3_gebaude.drop(i)
    fname = "onlyGebäude"
        
    return df3_gebaude, fname

def non_gebaude_only(df):
    df4_non_gebaude = df.copy()
    for i, text in enumerate(df4_non_gebaude['Gebäude/Geb./Geb/Bau']):
        if pd.isna(text):
            df4_non_gebaude = df4_non_gebaude.drop(i) 
        elif text.split()[0] in ["Gebäude"]:
        #print(text)
            df4_non_gebaude = df4_non_gebaude.drop(i)
        else:
            pass
    fname = "nonGebäude"
    
    
    return df4_non_gebaude, fname
    
    