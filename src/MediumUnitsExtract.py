#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 21:12:51 2021

@author: khazi
"""
import pandas as pd

def MediumUnitsExtract(df):
    
    storm_list = []
    wärme_list = []
    Trinkwasser_list = []
    VE_Wasser_list = []
    Chemie_abwasser_list = []
    Druckluft_list = []
    Regenwasser_list = []
    Kühlwasser_list = []
    Gas_list = []
    Fehlwasser_list = []
    Brauchwasser_list = []
    Stickstoff_list = []
    mediumDict = {}
    
    unique_medium = df['Medium'].unique()
    df_mediumUnit = df[['Medium', 'Bm_zw_ausgang_einheit']].copy()


    for i, medium in enumerate(df_mediumUnit['Medium']):
        if medium == unique_medium[0]:
            storm_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[1]:
            wärme_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[2]:
            Trinkwasser_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[3]:
            VE_Wasser_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[4]:
            Chemie_abwasser_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[5]:
            Druckluft_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[6]:
            Regenwasser_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[7]:
            Kühlwasser_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[8]:
            Gas_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[9]:
            Fehlwasser_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[10]:
            Brauchwasser_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])
        elif medium == unique_medium[11]:
            Stickstoff_list.append(df_mediumUnit['Bm_zw_ausgang_einheit'][i])    
    
    

    mediumDict['Strom'] = list(set(storm_list))
    mediumDict['wärme'] = list(set(wärme_list))
    mediumDict['Trinkwasser'] = list(set(Trinkwasser_list))
    mediumDict['VE_Wasser'] = list(set(VE_Wasser_list))
    mediumDict['Chemie_abwasser'] = list(set(Chemie_abwasser_list))
    mediumDict['Druckluft'] = list(set(Druckluft_list))
    mediumDict['Regenwasser'] = list(set(Regenwasser_list))
    mediumDict['Kühlwasser'] = list(set(Kühlwasser_list))
    mediumDict['Gas'] = list(set(Gas_list))
    mediumDict['Fehlwasser'] = list(set(Fehlwasser_list))
    mediumDict['Brauchwasser'] = list(set(Brauchwasser_list))
    mediumDict['Stickstoff'] = list(set(Stickstoff_list))

    
    multiple_units_per_medium = pd.DataFrame(mediumDict.items(), columns= ['Medium', 'Unit'] ) 
    fileName = "multiple_units_per_medium"
    
    return multiple_units_per_medium, fileName


#    multiple_units_per_medium.to_csv('multiple_units_per_medium.csv', sep= ';')
#    multiple_units_per_medium.to_excel('multiple_units_per_medium.xlsx', index = False)
            

    
    