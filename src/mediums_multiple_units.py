#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 23:30:37 2021

@author: khazi
"""

# saperate indices for all the mediums with multiple units
def mediums_multiple_units(df):
        
    strom_index = []
    druckluft_index = []
    regenwasser_index = []
    gas_index = []
    trinkwasser_index = []
    warmwasser_index = []
    
    
    for i, name in enumerate(df['Medium']):
        if name == "Strom":
            strom_index.append(i)
        elif name == "Regenwasser":
            regenwasser_index.append(i)
        elif name == "Druckluft":
            druckluft_index.append(i)
        elif name == "Gas":
            gas_index.append(i)
        elif name == "Wärme":
            warmwasser_index.append(i)
        else:
            pass
    
    df_strom        = df.iloc[strom_index,:]
    df_druckluft    = df.iloc[druckluft_index,:]
    df_regenwasser  = df.iloc[regenwasser_index,:]
    df_gas          = df.iloc[gas_index,:]
    df_trinkwasser  = df.iloc[trinkwasser_index,:]
    df_warmwasser   = df.iloc[warmwasser_index,:]
    
    
    return df_strom, df_druckluft, df_regenwasser,df_gas, df_trinkwasser, df_warmwasser