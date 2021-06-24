#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:55:03 2021

@author: khazi
"""


def to_csv_xls(df, rootPath, Fname):


    #df2 creates a valid comments as csv file
    df.to_csv(rootPath + '/csvFiles/' + Fname + '.csv' , encoding='utf-8', sep= ';')
    #df2.to_csv(rootPath + '/df_with_valid_komments_semicolon.csv', encoding='utf-8', sep= ';')
    df.to_excel(rootPath + '/xlsFiles/' + Fname + '.xlsx', index = False)