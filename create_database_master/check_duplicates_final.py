"""
This file contains the function to check for duplicates in the spreadsheet.
This is a specialised database that has three columns that makes up a unique key.

The Station name, the System and the Tag number.

As the sheet being checked is on a station basis only the System and Tag number are
checked for duplicates.


"""

import create_database_master.src.duplicates as dup
import src.excel_io_dataframe as xl
import pandas as pd

file_path = '../data/Steamfield_master_2024_02_03.xlsx'  # Replace this with the path to your workbook
data_base = xl.read_workbook(file_path, -1, 0)
#print(data_base.iloc[:5, 0:8])

dup.check_for_duplicates(data_base, 'System', 'Tag')