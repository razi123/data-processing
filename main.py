#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 14:20:01 2021

@author: khazi
"""

import pandas as pd
from src import df_class, to_csv_xls, MediumUnitsExtract, gebaude_Nongebaude_Extract,TotalMediumCount, Valid_Invalid_Buildings
from src import mediums_multiple_units, Gebaude_NonGebaude_Split as gns, anlageMediumsCount as amc, excel_cases as ecase, meter_replaement_date_time as edtc 

def main():


    rootPath = '/Users/khazi/Documents/HiWi/spyderCode'
    dframe = pd.read_csv(rootPath + '/dataset' + "/metadata_campus_nord_with_valid_from.csv", sep=';') # metadata_campus_nord_with_valid_from
    df_excel_cases = pd.read_excel(rootPath + '/dataset' + "/df_with_valid_komments_excel.xlsx")
    
    df_processed = df_class.Pre_processing(dframe);
    df_datetime = df_class.DateTime_Pattern(df_processed);
    df_comments_drop, fname = df_class.DropComments(df_datetime,rootPath);
    
    to_csv_xls.to_csv_xls(df_comments_drop, rootPath, fname);
    
    df_multUnits_per_Medium, mediumName = MediumUnitsExtract.MediumUnitsExtract(df_processed)
    to_csv_xls.to_csv_xls(df_multUnits_per_Medium, rootPath, mediumName);
    
    
    # Gebaude_NonGebaude extracts
    df_gebaude                        = gebaude_Nongebaude_Extract.gebaudeExtract(df_datetime)
    df_geb_non_geb                    = gebaude_Nongebaude_Extract.NonGebaudeExtract(df_gebaude)
    
    
    geb_only, geb_only_name           = gebaude_Nongebaude_Extract.gebaude_only(df_geb_non_geb)
    to_csv_xls.to_csv_xls(geb_only, rootPath, geb_only_name);
    
    
    non_geb_only, non_geb_only_name   = gebaude_Nongebaude_Extract.non_gebaude_only(df_geb_non_geb)
    to_csv_xls.to_csv_xls(non_geb_only, rootPath, non_geb_only_name);
    
    
    TotalMediumCount.TotalMediumCount(df_geb_non_geb)
    df_vld_build, df_not_vld_build, df_NonNumericBuildings = Valid_Invalid_Buildings.Valid_Invalid_Buildings(df_geb_non_geb)
    

    to_csv_xls.to_csv_xls(df_vld_build, rootPath, "ValidBuildingNumbers")
    to_csv_xls.to_csv_xls(df_not_vld_build, rootPath, "InvalidBuildingNumbers")
    to_csv_xls.to_csv_xls(df_NonNumericBuildings, rootPath, "NonNumericBuildingNumbers")
    
    
    # mediums with multiple units
    df_strom, df_druckluft, df_regenwasser,df_gas, df_trinkwasser, df_warmwasser = mediums_multiple_units.mediums_multiple_units(df_geb_non_geb)
    to_csv_xls.to_csv_xls(df_strom, rootPath, "df_strom_units_only")
    to_csv_xls.to_csv_xls(df_druckluft, rootPath, "df_druckluft_units_only")
    to_csv_xls.to_csv_xls(df_regenwasser, rootPath, "df_regenwasser_units_only")
    
    
    to_csv_xls.to_csv_xls(df_gas, rootPath, "df_gas_units_only")
    to_csv_xls.to_csv_xls(df_trinkwasser, rootPath, "df_trinkwasser_units_only")
    to_csv_xls.to_csv_xls(df_warmwasser, rootPath, "df_warmwasser_units_only")
    
    
    df_gebaude_rows_only, df_non_gebaude_rows_only = gns.Gebaude_NonGebaude_Split(df_geb_non_geb)    
    to_csv_xls.to_csv_xls(df_gebaude_rows_only, rootPath, "df_gebaude_geb_bau_rows_only")
    to_csv_xls.to_csv_xls(df_non_gebaude_rows_only, rootPath, "df_non_gebaude_rows_only")
    
    
    
    MediumsCount = amc.AnlageMediumCount(df_geb_non_geb)
    to_csv_xls.to_csv_xls(MediumsCount, rootPath, "anlageMediumsCount")
    
    
    gebaudeMediumsCount, total_mediums_per_buildings = amc.GebaudeCount(df_geb_non_geb)
    to_csv_xls.to_csv_xls(gebaudeMediumsCount, rootPath, "gebaudeMediumsCount")
    to_csv_xls.to_csv_xls(total_mediums_per_buildings, rootPath, "total_mediums_per_buildings")
    
    
    df_further_info,df_ignore,df_meter_replacement,df_null_values,df_valid_until_dismantle,\
        df_change_measured_buildings,df_change_pulse_value, df_change_of_use, df_meter_dependency, df_converter_change, \
            df_valid_from, df_invalid_from, df_converter_programmed, df_converter_correction = ecase.excelCases(df_excel_cases)
            
            
    to_csv_xls.to_csv_xls(df_meter_replacement, rootPath, "df_meter_replacement")
    
    #df_meter_replacement_1 = edtc.meter_replace_datetime(rootPath, "df_meter_replacement")
    #to_csv_xls.to_csv_xls(df_meter_replacement_1, rootPath, "df_meter_replacement_1")
    
    
    
    
    
    
    
    #to_csv()
    
    
    
                                
                                
                                
if __name__ == "__main__" :
    main()
    
