### Ich könnte nicht die dataset zu teilen, weil ich nicht durfen ist. Die Dataset ist komplett kaputt und die python code kann nur 60% wichtige information extrahieren.### 
# Ich vorbereite noch python script weiter wichtige information zu extrahieren ###  
# Aber Kann ich etwas üben die Datei teilen: Die datei is die meta-data von Universität campus, es hat 15 verschiedene Messe-sensoren,2200 insgesamt meta-data record, mit 22 Features ###
# 22 Columns sind Anlage, Gebäude, Kommentare(Text datei), Datum, Messeiheit,Messe von Sensor usw ### 
# Die datei ist komplett kaputt ###    
# Am ende alle Extrahieren Datei für weitere ananlysis wird in .csv and .xls konvertieren ###

 

# src folder has 11 python files(Modules)

   1. df_class.py                   : vorbearbeitung die raw dataset mit Text datei, Date-Time pattern Extrahieren **(Bib : RegEx, Datetime, Numpy, Pandas)**
   
   2. Gebaude_NonGebaude_Split.py   : nur gültiges Gebäude von Dataframe split **(Bib: NLTK- Bag of wrods and Tokenization)**
   
   3. MediumUnitsExtracts.py        : Alle Medium und Messeinheiten Extrahieren als DataFrame **(Bib: Pandas)**
   
   4. TotalMediumCount.py           : Extrahieren Wie Viel Sensor units pro Medium 
   
   5. Valid_invalid_Buildings.py    : Auf dem DataFrame Extrahierte Wie viele wichtige gebäude in Campus (Bib: )
   
   6. AnlageMediumsCount.py         : Wie viele Anlage zahlen pro Gebäude
   
   7. Excel-cases.py                : [Messstelle, Kommentare, Date] extrahieren
   
   8. Gebaude_Nongebaude_Extract.py : nur gültiges Gebäude von Dataframe extrahieren **(Bib: NLTK, Pandas, Numpy, RegEx)**
   
   9. Mediums_multiple_units.py     : Nur mediums mit mehr einheiten extrahieren für weiter anfragen
   
   10. meter_replacement_date_time   : Mediums replacement date time extrahieren **Bib: RegEx, Numpy, NLTK, datefinder)**
   
   11. to_csv_xls.py                 : Alle DataFrames nach extrahieren wird zu CSV und Excel Konvertieren. 

   
 
