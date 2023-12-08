"""
This script is to filter through the new and subsequent instrument lists
and convert it into a database format that can be sucked into the Contact instrument database

Put the sheets with the names of:

    instrument_master.xls as the master instrument.
    database_master as the file that is getting edited.

    Make sure that there are no duplicates in the spreadsheet.

    Remove anything above and below the spreadsheet.
    We only want the single header at the top and no notes or anything irrelevant at the bottom of the
    sheet.

"""
"""
This script is to filter through the new and subsequent instrument lists
and convert it into a database format that can be sucked into the Contact instrument database

Put the sheets with the names of:

    instrument_master.xls as the master instrument.
    database_master as the file that is getting edited.

    Make sure that there are no duplicates in the spreadsheet.

    Remove anything above and below the spreadsheet.
    We only want the single header at the top and no notes or anything irrelevant at the bottom of the
    sheet.

"""

from create_database_master.src import excel_io_dataframe as xl, wrangle_database_master as wr

# read instrument Database lists|
# TODO select for full list
# file_path = '../data/database_master.xlsx'  # Replace this with the path to your workbook 1
# TODO select for reducest list for testing
file_path = '../data/database_master_shortList.xlsx'  # Replace this with the path to your workbook 1

instrument_data_list_df = xl.read_workbook(file_path, -1, 0)

# read instrument master lists|
# TODO select for full list
# file_path = '../data/instrument_master.xlsx'  # Replace this with the path to your workbook 2
# TODO select for reducest list for testing
file_path = '../data/instrument_master_shortList.xlsx'  # Replace this with the path to your workbook 2

instrument_master_list_df = xl.read_workbook(file_path, -1, 0)

# Version of instrument master lists
version: str = '7.6'

# Wrangle  data

xl.create_excel_from_dataframe(wr.wrangle_database_list(instrument_master_list_df,
                                                        instrument_data_list_df, version=''), '../data/generated_database.xlsx')

if instrument_master_list_df is not None:
    print("Dataframe contents:")
    # print(instrument_d_list_df)
