"""

Abbreviate the text in a specific column of the dataframe.
Use the Contact Energy standard document number 10000002582 revision 2
to abbreviate the text in the dataframe.

"""

import src.excel_io_dataframe as xl
import src.abbreviate as ab

# read instrument Database lists|/
file_path = '../data/generated_database_v6.0.xlsx'  # Replace this with the path to your workbook 1
data_base = xl.read_workbook(file_path, -1, 0)

# Abbreviate the text in the dataframe column called 'System'
ab.abbreviate_text(data_base, 'System', '../Data/ContactEnergy_abbreviations.xlsx', '')

