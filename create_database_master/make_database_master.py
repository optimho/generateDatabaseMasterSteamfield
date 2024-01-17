"""
This script is to filter through the database Master and modify information

Put the sheets with the names of:

    instrument_master.xls as the master instrument.
    database_master as the file that is getting edited.

    Make sure that there are no duplicates in the spreadsheet.

    Remove anything above and below the spreadsheet.
    We only want the single header at the top and no notes or anything irrelevant at the bottom of the
    sheet.

    Read the README.md for more information.

"""

from create_database_master.src import excel_io_dataframe as xl, wrangle_database_master as wr
from create_database_master.src import excel_to_dict as ed

# read instrument Database lists|
# TODO select for full list
# file_path = '../data/database_master.xlsx'  # Replace this with the path to your workbook 1
# TODO select for reducest list for testing
file_path = '../Data/Templates Entry Instrument Full.xlsx'  # Replace this with the path to your workbook 1

instrument_data_list_df = xl.read_workbook(file_path, -1, 0)

# read instrument master lists|
#
file_path = '../Data/TABG-CEL-0-000-CCI-LST-1401_7.8.xlsx'  # Replace this with the path to your workbook 2
instrument_master_list_df = xl.read_workbook(file_path, -1, 0)

# read the list of KKS SYSTEM codes from an Excel spreadsheet
file_path = '../Data/KKS_SYSTEMS.xlsx'
# kks_systems_df = xl.read_workbook(file_path, -1, 0)
kks_system_dict = ed.excel_to_dict(file_path)

# Version of instrument master lists
version: str = '6.0'

# Wrangle  data
xl.create_excel_from_dataframe(wr.modify_database_list(instrument_master_list_df, instrument_data_list_df, version),
                               f'../data/generated_database_v{version}.xlsx')

if instrument_master_list_df is not None:
    print("Dataframe contents:")
    # print(instrument_d_list_df)