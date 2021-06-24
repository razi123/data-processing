#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 23:47:30 2021

@author: khazi
"""

import pandas as pd

def AnlageMediumCount(df):
    # pair for anlage and mediums 
    buildingMediums = df[['Anlage', 'Medium']]
    
    # Count the total mediums in each anlage 
    anlageMediumsCount = df.groupby(['Anlage','Medium'])['Medium'].count().reset_index(name="Count")
    
    # Export to csv and excel total mediums in each anlage
    return anlageMediumsCount



def GebaudeCount(df):
# Count the total mediums in each anlage 
    gebaudeMediumsCount = df.groupby(['Gebaeude', 'Medium'])['Medium'].count().reset_index(name="count")
    # create a dataframe that contain the total number of meters per buildings

    keys = list(gebaudeMediumsCount['Gebaeude'].unique())
    medium_dict = dict.fromkeys(keys, 0)
    temp = 0

    for idx, txt in enumerate(gebaudeMediumsCount['Gebaeude']):
        #print(txt)
        temp = medium_dict[txt] 
        temp = temp + gebaudeMediumsCount['count'][idx]
        medium_dict[txt] = temp
        
        temp = 0
        
    total_mediums_per_buildings = pd.DataFrame(medium_dict.items())
    total_mediums_per_buildings = total_mediums_per_buildings.rename(columns={0: "Anlage", 1: "Mediums"})
    
    return gebaudeMediumsCount,total_mediums_per_buildings