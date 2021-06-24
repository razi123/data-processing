#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 11:00:33 2021

@author: khazi
"""
import pandas as pd
import nltk
import re
import datefinder

def meter_replace_datetime(rootPath, fName):
    #df2 creates a valid comments as csv file
    #df.to_csv(rootPath + '/csvFiles/' + Fname + '.csv' , encoding='utf-8', sep= ';')
    
    df_meter_replacement = pd.read_csv(rootPath + '/csvFiles/' + fName +  '.csv', error_bad_lines=False) # metadata_campus_nord_with_valid_from
    
    xtenceArray = []
    bagWords = []
    dateTime = []
    temp = []
    timePattern_1 = r'[0-9]{1,2}\:[0-9]{1,2}'
    datePattern_2 = r'([A-Za-zä]{3,9}[0-9]{4})'
    datePattern_3 = r'([A-Za-zä]{3,9} [0-9]{4})'
    months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober','November', 'Dezember', 'Feb']
    df_meter_replacement['Dates'] = " "
    df_meter_replacement['Time'] = " "
    
    sentenceBag = df_meter_replacement['Kommentare']
    
    for xtences in sentenceBag:
        xtenceArray.append(xtences)
    
    for xtence in xtenceArray:
        Token = nltk.word_tokenize(str(xtence))
        bagWords.append(Token)
    
    
    for idx, dtime in enumerate(xtenceArray):
        matches = datefinder.find_dates(str(dtime))
        if re.search(datePattern_3, dtime): # july wala pattern
            temp1 = re.findall(datePattern_3, dtime)
            newlist = [word for line in temp1 for word in line.split(' ')]
            
            for ind, nl in enumerate(newlist):
                if nl in months:
                    xtx = nl + ' '+ newlist[ind+1]
                    df_meter_replacement['Dates'][idx] = xtx
                    #for dt in matches:
                    #    df_meter_replacement['DateTime'][idx] = '1' #dt.time()
        else: 
            for dt in matches:
                df_meter_replacement['Dates'][idx] = dt.date()
    
    
    # for time            
    for idx, dtime in enumerate(xtenceArray):
        matches = datefinder.find_dates(str(dtime))
        if re.search(timePattern_1, dtime): # july wala pattern
            for dt in matches:
                df_meter_replacement['Time'][idx] = dt.time()
        else:
            pass
    
    return df_meter_replacement
        
    
    