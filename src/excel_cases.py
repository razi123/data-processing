#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 08:21:52 2021

"""

def excelCases(df_excel_cases):
    # select only first 285 rows
    df_split = df_excel_cases.iloc[:,:]
    
    # indices with 
    index_case_minus_1 = []
    index_case_0 = []
    index_case_1 = []
    index_case_2 = []
    index_case_3 = []
    index_case_4 = []
    index_case_5 = []
    index_case_6 = []
    index_case_7 = []
    index_case_8 = []
    index_case_9 = []
    index_case_10 = []
    index_case_11 = []
    index_case_12 = []
    index_case_13 = []
    
    
    for idx, text in enumerate(df_split['Case']):
        temp = str(text)
    
        for el in temp.split(','):
            if int(el) == -1:
                index_case_minus_1.append(idx)
            elif int(el) == 0:
                index_case_0.append(idx)
            elif int(el) == 1:
                index_case_1.append(idx)
            elif int(el) == 2:
                index_case_2.append(idx)
            elif int(el) == 3:
                index_case_3.append(idx)
            elif int(el) == 4:
                index_case_4.append(idx)
            elif int(el) == 5:
                index_case_5.append(idx)
            elif int(el) == 6:
                index_case_6.append(idx) 
            elif int(el) == 7:
                index_case_7.append(idx) 
            elif int(el) == 8:
                index_case_8.append(idx) 
            elif int(el) == 9:
                index_case_9.append(idx) 
            elif int(el) == 10:
                index_case_10.append(idx)
            elif int(el) == 11:
                index_case_11.append(idx) 
            elif int(el) == 12:
                index_case_12.append(idx)
            elif int(el) == 13:
                index_case_12.append(idx)
    
    
    
    indexList = [index_case_minus_1, index_case_0, index_case_1, index_case_2, index_case_3, index_case_4, index_case_5, 
             index_case_6, index_case_7, index_case_8, index_case_9, index_case_10, index_case_11,index_case_12, 
             index_case_13]

    for idx in indexList:
        df_temp = df_split.iloc[idx,:]
        
        if idx == index_case_minus_1:
            df_further_info = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_0:
            df_ignore = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_1:
            df_meter_replacement = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_2:
            df_null_values = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_3:
            df_valid_until_dismantle = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_4:
            df_change_measured_buildings = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_5:
            df_change_pulse_value = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_6:
            df_change_of_use = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_7:
            df_meter_dependency = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_8:
            df_converter_change = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_9:
            df_valid_from = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_10:
            df_invalid_from = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_11:
            df_converter_programmed = df_temp[['Messstelle', 'Kommentare', 'Date']]
        elif idx == index_case_12:
            df_converter_correction = df_temp[['Messstelle', 'Kommentare', 'Date']]
        else:
            pass
        
    
    return (df_further_info,df_ignore,df_meter_replacement, df_null_values,df_valid_until_dismantle,df_change_measured_buildings,  
        df_change_pulse_value, df_change_of_use, df_meter_dependency, df_converter_change, df_valid_from, 
        df_invalid_from, df_converter_programmed, df_converter_correction)
    
    
            
        
        
        