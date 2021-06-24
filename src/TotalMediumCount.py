#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 22:40:36 2021

@author: khazi
"""

def TotalMediumCount(df):
    df_test = df.groupby(['Medium', 'Bm_zw_ausgang_einheit'])['Bm_zw_ausgang_einheit'].count().reset_index(name='Count')
    

def MediumCount(df):
    
    mediumRows = {}

    Strom = []
    Brauchwasser = []
    ChemieAbwasser = []
    Fehlwasser = []
    
    Druckluft = []
    Gas = []
    Kühlwasser = []
    Regenwasser = []
    
    Stickstoff = []
    Trinkwasser = []
    VE_Wasser = []
    Wärme = []
    
    
    for i, item in enumerate(df['Medium']):
        if item == "Strom":
            Strom.append(i)
        elif item == "Brauchwasser":
            Brauchwasser.append(i)
        elif item == "Chemie-Abwasser":
            ChemieAbwasser.append(i)
        elif item == "Fehlwasser":
            Fehlwasser.append(i)
        elif item == "Gas":
            Gas.append(i)
        elif item == "Kühlwasser":
            Kühlwasser.append(i)
        elif item == "Regenwasser":
            Regenwasser.append(i)
        elif item == "Stickstoff":
            Stickstoff.append(i)
        elif item == "Trinkwasser":
            Trinkwasser.append(i)
        elif item == "VE-Wasser":
            VE_Wasser.append(i)
        elif item == "Wärme":
            Wärme.append(i)
        elif item == "Druckluft":
            Druckluft.append(i)
        else:
            pass
        
                        
    mediumRows['Strom'] = Strom
    mediumRows['Brauchwasser'] = Brauchwasser
    mediumRows['ChemieAbwasser'] = ChemieAbwasser
    mediumRows['Fehlwasser'] = Fehlwasser
    
    mediumRows['Druckluft'] = Druckluft
    mediumRows['Gas'] = Gas
    mediumRows['Kühlwasser'] = Kühlwasser
    mediumRows['Regenwasser'] = Regenwasser
    
    mediumRows['Stickstoff'] = Stickstoff
    mediumRows['Trinkwasser'] = Trinkwasser
    mediumRows['VE_Wasser'] = VE_Wasser
    mediumRows['Wärme'] = Wärme    