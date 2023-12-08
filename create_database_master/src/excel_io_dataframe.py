" Open a excel file and converts it to a Pandas dataframe "

import pandas as pd
import os

def read_workbook(filename, dropNum, headerNum):
    try:
        # Read the workbook
        xl: pd = pd.ExcelFile(filename)

        # Assuming there's only one sheet in the workbook
        sheet_name = xl.sheet_names[0]

        # Read the sheet into a pandas DataFrame and change NANs to empty strings
        if (headerNum == -1):
            df = pd.read_excel(filename, sheet_name=sheet_name).fillna('')
        else:
            df = pd.read_excel(filename, sheet_name=sheet_name, header=headerNum).fillna('')

        # Assuming dataframe is your Pandas DataFrame and row_index is the index of the row you want to drop
        if dropNum == -1:
            return df
        else:
           df = df.drop(dropNum)
        return df

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def create_excel_from_dataframe(df, filename):
    try:
        # Export DataFrame to Excel workbook
        df.to_excel(filename, index=True)

        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"    Excel file '{filename}' created successfully.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    except Exception as e:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"        An error occurred: {str(e)}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
