#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:25:48 2021

@author: khazi
"""
import pandas as pd
import re
import numpy as np
import csv
import datetime


   
def Pre_processing(df):
    """
    Rename columns, 
    Fill missing data in Anlage
    Proper rename Units in 
    
    
    """

    df = df.rename(columns = {'Kommentarenwi' : 'Kommentare'})
    df['Anlage']     = df['Messstelle'].apply(lambda x : x[0:4])
    df['Teilanlage'] = df['Messstelle'].apply(lambda y : y[5:9])
    df['Modul']      = df['Messstelle'].apply(lambda z : z[10:]+z[5:9])
    df['Gebaeude']   = df['Messstelle'].apply(lambda x1 : x1[0:4])
    
    # Proper rename and align the measuring units 
    df['Bm_zw_ausgang_einheit'] = df['Bm_zw_ausgang_einheit'].replace('m2', 'm\u00B2')
    df['Bm_zw_ausgang_einheit'] = df['Bm_zw_ausgang_einheit'].replace('m3', 'm\u00B3')
    df['Bm_zw_ausgang_einheit'] = df['Bm_zw_ausgang_einheit'].replace('Nm3', 'Nm\u00B3')
    df['Bm_zw_ausgang_einheit'] = df['Bm_zw_ausgang_einheit'].replace('kwh', 'kWh')
    
    
    return df



def DateTime_Pattern(df):

    df['Date'] = ""
    df['Time'] = ""
    dictYear = {}
    dictTime = {}
    
    datePattern_1 = r'[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{2,4}'
    datePattern_2 = r'([A-Za-zä]{3,9}[0-9]{4})'
    datePattern_3 = r'([A-Za-zä]{3,9} [0-9]{4})'
    #datePattern_3 = r'([A-Za-zä-]{3,9}[0-9]{4} )'
    datePattern_4 = r'([0-9]{2}\/[0-9]{2,4})'
    #datePattern_5 = r'([0-9]{1,2}\.[0-9]{2,4})'
    
    timePattern_1 = r'[0-9]{1,2}\:[0-9]{1,2}'
    months = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober','November', 'Dezember', 'Feb']
    
    #print(pd.isnull(df['Kommentare']))
    for idx, sentence in enumerate(df['Kommentare']):
        if pd.isnull(sentence):
            dictYear[idx] = "NaN"
            dictTime[idx] = "NaN"
        else:
            #print(idx)
            if re.search(datePattern_1, sentence):
                dictYear[idx] = re.findall(datePattern_1, sentence)
                if re.search(timePattern_1, sentence):
                    dictTime[idx] = re.findall(timePattern_1, sentence)
                    
            elif re.search(datePattern_2, sentence):
                dictYear[idx] = re.findall(datePattern_2, sentence)
                    
            elif re.search(datePattern_3, sentence):
                dictYear[idx] = re.findall(datePattern_3, sentence)
                        
            elif re.search(datePattern_4, sentence):
                dictYear[idx] = re.findall(datePattern_4, sentence)
                
        
    for i, value in dictYear.items():
        df['Date'][i] = value
    
    for i, value in dictTime.items():
        df['Time'][i] = value
    
    return df


def DropComments(df,rootPath):
    df2 = df.copy()
    df2['Kommentare'] = df2['Kommentare'].replace(r'\\N',np.nan, regex=True) 
    df2['Kommentare'] = df2['Kommentare'].dropna()

    with open(rootPath + '/csvFiles' +  "/Kommentare.csv", 'w', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow(['Sl No', 'Kommentare'])
        for i, text in enumerate(df2['Kommentare']):
            if pd.isna(text):
                df2 = df2.drop(i)
            else:
                writer.writerow([i, text])
    fileName = "df_with_valid_komments"
    return df2, fileName
    
    
            
        
          
          